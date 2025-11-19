#version 330

in vec2 v_uv;
out vec4 f_color;

uniform sampler2D Texture;

uniform vec2 seed;
uniform int iter;

void main() {
    vec2 c = seed;
    int i;

    vec2 z = v_uv * vec2(2.0, 2.0);

    for(i = 0; i < iter; i++) {
        float x = (z.x * z.x - z.y * z.y) + c.x;
        float y = (z.y * z.x + z.x * z.y) + c.y;

        if((x * x + y * y) > 4.0) {
            break;
        }

        z.x = x;
        z.y = y;
    }

    f_color = texture(Texture, vec2((i == iter ? 0.0 : float(i)) / 100.0, 0.0));
}