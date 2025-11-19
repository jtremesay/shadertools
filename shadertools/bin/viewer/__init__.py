import os
from pathlib import Path

import moderngl_window as mglw
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("shadertools"))


def get_f_user_shader():
    return Path("shader.fs").read_text()


def get_f_shader(f_user_shader):
    f_shader_tpl = env.get_template("shaders/main.fs")
    return f_shader_tpl.render(user_shader=f_user_shader)


class ShaderViewer(mglw.WindowConfig):
    title = "Resource Loading with ModernGL Window"
    resizable = False
    gl_version = (3, 3)
    window_size = (1024, 1024)
    aspect_ratio = 1.0
    resource_dir = os.path.normpath(os.path.join(__file__, "../../../data"))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        f_shader = get_f_shader(get_f_user_shader())
        v_shader = (Path(self.resource_dir) / "shaders" / "main.vs").read_text()
        self.program = self.ctx.program(
            vertex_shader=v_shader, fragment_shader=f_shader
        )
        self.vao = self.ctx.vertex_array(self.program, [])
        self.vao.vertices = 3
        self.frame = 0

    def on_render(self, time, frame_time):
        print(time, frame_time)
        self.ctx.clear()

        # Theses uniforms are optional in the shader, and may not be present
        try:
            self.program["iResolution"] = [
                self.window_size[0],
                self.window_size[1],
                0.0,
            ]
        except KeyError:
            pass

        try:
            self.program["iTime"] = time
        except KeyError:
            pass
        try:
            self.program["iTimeDelta"] = frame_time
        except KeyError:
            pass

        try:
            self.program["iFrameRate"] = 60
        except KeyError:
            pass

        try:
            self.program["iFrame"] = self.frame
        except KeyError:
            pass

        try:
            self.program["iChannelTime"] = [0, 0, 0, 0]
        except KeyError:
            pass

        try:
            self.program["iChannelResolution"] = [0, 0, 0, 0]
        except KeyError:
            pass

        try:
            self.program["iMouse"] = (0.0, 0.0, 0.0, 0.0)
        except KeyError:
            pass

        self.vao.render()
        self.frame += 1


def main():
    ShaderViewer.run()
