vec3 canvas_to_viewport(vec2 pixel_coord) {
    vec3 uv = vec3(pixel_coord, 1.0) / vec3(iResolution.xy, 1.0);
    uv = uv * 2.0 - 1.0;
    uv.x *= iResolution.x / iResolution.y;
    return uv;
}

vec3 trace_ray(vec3 origin, vec3 direction, float t_min, float t_max) {
    // Simple gradient background
    float t = 0.5 * (direction.y + 1.0);
    vec3 white = vec3(1.0, 1.0, 1.0);
    vec3 blue = vec3(0.5, 0.7, 1.0);
    return mix(white, blue, t);
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec3 direction = canvas_to_viewport(fragCoord);
    vec3 origin = vec3(0.0, 0.0, 0.0);
    vec3 color = trace_ray(origin, direction, 1.0, 100.0);

    // Output to screen
    fragColor = vec4(color, 1.0);
}