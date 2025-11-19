from shadertools.compiler import (
    compile_scene_to_shadertoy_shader,
    compile_shadertoy_shader_to_glsl_shader,
    glsl_vec3,
)
from shadertools.math import Vec3
from shadertools.scene import Scene


class TestFilters:
    def test_glsl_vec3(self):
        v = Vec3(1.0, 2.0, 3.0)
        result = glsl_vec3(v)
        assert result == "vec3(1.0, 2.0, 3.0)"


class TestSTCompiler:
    def test_compile_scene_to_shadertoy_shader(self):
        scene = Scene()
        compile_scene_to_shadertoy_shader(scene)


class TestGLSLCompiler:
    def test_full_compilation_pipeline(self):
        scene = Scene()
        shadertoy_shader = compile_scene_to_shadertoy_shader(scene)
        compile_shadertoy_shader_to_glsl_shader(shadertoy_shader)
