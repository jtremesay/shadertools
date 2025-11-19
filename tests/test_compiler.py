from shadertools.compiler import (
    compile_scene_to_shadertoy_shader,
    compile_shadertoy_shader_to_glsl_shader,
    glsl_vec3,
)
from shadertools.math import Vec3


class TestFilters:
    def test_glsl_vec3(self):
        v = Vec3(1.0, 2.0, 3.0)
        result = glsl_vec3(v)
        assert result == "vec3(1.0, 2.0, 3.0)"


class TestSTCompiler:
    def test_compile_scene(self, scene, ref_st_shader):
        st_shader = compile_scene_to_shadertoy_shader(scene)
        assert st_shader == ref_st_shader


class TestGLSLCompiler:
    def test_compile_scene(self, scene, ref_glsl_shader):
        st_shader = compile_scene_to_shadertoy_shader(scene)
        glsl_shader = compile_shadertoy_shader_to_glsl_shader(st_shader)
        assert glsl_shader == ref_glsl_shader
