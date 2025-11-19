from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("shadertools"))


def compile_scene_to_shadertoy_shader(scene) -> str:
    tpl = env.get_template("shaders/shadertoy.fs")
    return tpl.render(scene=scene)


def compile_shadertoy_shader_to_glsl_shader(shadertoy_shader: str) -> str:
    tpl = env.get_template("shaders/main.fs")
    return tpl.render(user_shader=shadertoy_shader)
