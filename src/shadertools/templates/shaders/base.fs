{#-
ANTI-CAPITALIST SOFTWARE LICENSE (v 1.4)

Copyright © 2025 Jonathan Tremesayques

This is anti-capitalist software, released for free use by individuals and 
organizations that do not operate by capitalist principles.

Permission is hereby granted, free of charge, to any person or organization 
(the "User") obtaining a copy of this software and associated documentation 
files (the "Software"), to use, copy, modify, merge, distribute, and/or sell 
copies of the Software, subject to the following conditions:

  1. The above copyright notice and this permission notice shall be included 
     in all copies or modified versions of the Software.

  2. The User is one of the following:
    a. An individual person, laboring for themselves
    b. A non-profit organization
    c. An educational institution
    d. An organization that seeks shared profit for all of its members, and 
       allows non-members to set the cost of their labor

  3. If the User is an organization with owners, then all owners are workers 
    and all workers are owners with equal equity and/or equal vote.

  4. If the User is an organization, then the User is not law enforcement or 
     military, or working for or under either.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT EXPRESS OR IMPLIED WARRANTY OF ANY 
KIND, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS 
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE 
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-#}

{%- import "shaders/utils.fs" as utils -%}

{# TODO: Make these camera parameters dynamic #}

const float NEAR = 1.0;
const float FAR = 100.0;
const vec3 ORIGIN = {{ utils.glsl_vec3(scene.camera.position) }};
const vec3 VIEW_PORT = {{ utils.glsl_vec3(scene.camera.view_port) }};

const vec3 C_BACKGROUND_1 = vec3(1.0, 1.0, 1.0); // white
const vec3 C_BACKGROUND_2 = vec3(0.5, 0.7, 1.0); // light blue

// Declare some spheres
struct Sphere {
    vec3 center;
    float radius;
    vec3 color;
};

const int NUM_SPHERES = {{ scene.spheres|length }};
const Sphere spheres[NUM_SPHERES] = Sphere[](
{%- for sphere in scene.spheres %}
    Sphere({{ utils.glsl_vec3(sphere.center) }}, {{ sphere.radius|float }}, {{ utils.glsl_vec3(sphere.material.color) }}){{ "," if not loop.last }}
{%- endfor %}
);

vec3 canvas_to_viewport(vec2 pixel_coord) {
    vec2 uv = pixel_coord / iResolution.xy;
    uv = uv * 2.0 - 1.0;
    uv.x *= iResolution.x / iResolution.y;
    return vec3(uv, 1.0) * VIEW_PORT;
}

vec2 intersect_sphere(vec3 origin, vec3 direction, int sphere_index) {
    Sphere sphere = spheres[sphere_index];
    vec3 oc = origin - sphere.center;

    float a = dot(direction, direction);
    float b = 2.0 * dot(oc, direction);
    float c = dot(oc, oc) - sphere.radius * sphere.radius;

    float discriminant = b * b - 4.0 * a * c;
    if (discriminant < 0.0) {
        return vec2(-1.0, -1.0); // No intersection
    } else {
        float t1 = (-b - sqrt(discriminant)) / (2.0 * a);
        float t2 = (-b + sqrt(discriminant)) / (2.0 * a);
        return vec2(t1, t2);
    }
}

vec3 trace_ray(vec3 origin, vec3 direction, float t_min, float t_max) {
    float closest_t = t_max;
    int closest_sphere = -1;

    for (int i = 0; i < NUM_SPHERES; i++) {
        vec2 t = intersect_sphere(origin, direction, i);
        if (t.x >= t_min && t.x <= t_max && t.x < closest_t) {
            closest_t = t.x;
            closest_sphere = i;
        }

        if (t.y >= t_min && t.y <= t_max && t.y < closest_t) {
            closest_t = t.y;
            closest_sphere = i;
        }
    }

    if (closest_sphere != -1) {
        return spheres[closest_sphere].color;
    }

    // Simple gradient background
    float t = 0.5 * (direction.y + 1.0);
    return mix(C_BACKGROUND_1, C_BACKGROUND_2, t);
}

vec4 render_frag(vec2 frag_coord) {
    vec3 direction = canvas_to_viewport(frag_coord);
    vec3 color = trace_ray(ORIGIN, direction, NEAR, FAR);

    // Output to screen
    return vec4(color, 1.0);
}