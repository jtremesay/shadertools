const float NEAR = 1.0;
const float FAR = 100.0;
const vec3 ORIGIN = vec3(0.0, 0.0, 0.0);

const vec3 C_BACKGROUND_1 = vec3(1.0, 1.0, 1.0); // white
const vec3 C_BACKGROUND_2 = vec3(0.5, 0.7, 1.0); // light blue

vec3 canvas_to_viewport(vec2 pixel_coord) {
    vec3 uv = vec3(pixel_coord, 1.0) / vec3(iResolution.xy, 1.0);
    uv = uv * 2.0 - 1.0;
    uv.x *= iResolution.x / iResolution.y;
    return uv;
}

vec3 trace_ray(vec3 origin, vec3 direction, float t_min, float t_max) {
    // Simple gradient background
    float t = 0.5 * (direction.y + 1.0);
    return mix(C_BACKGROUND_1, C_BACKGROUND_2, t);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec3 direction = canvas_to_viewport(fragCoord);
    vec3 color = trace_ray(ORIGIN, direction, NEAR, FAR);

    // Output to screen
    fragColor = vec4(color, 1.0);
}