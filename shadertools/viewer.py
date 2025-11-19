import os
from argparse import ArgumentParser
from pathlib import Path

import moderngl_window as mglw


class ShaderViewer(mglw.WindowConfig):
    title = "Resource Loading with ModernGL Window"
    resizable = False
    gl_version = (3, 3)
    window_size = (1024, 1024)
    aspect_ratio = 1.0
    resource_dir = os.path.normpath(os.path.join(__file__, "../data"))

    @classmethod
    def add_arguments(cls: type["WindowConfig"], parser: ArgumentParser) -> None:
        parser.add_argument(
            "--shader-file",
            type=Path,
            default="shader.fs",
            help="Path to the fragment shader file.",
        )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.program = self.ctx.program(
            vertex_shader=(Path(self.resource_dir) / "shaders" / "main.vs").read_text(),
            fragment_shader=self.argv.shader_file.read_text(),
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
