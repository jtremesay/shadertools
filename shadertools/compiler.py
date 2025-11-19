from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("shadertools"))


def compile_scene_to_shadertoy_shader(scene) -> str:
    return ""


def compile_shadertoy_shader_to_glsl_shader(shadertoy_shader: str) -> str:
    f_shader_tpl = env.get_template("shaders/main.fs")
    return f_shader_tpl.render(user_shader=shadertoy_shader)
