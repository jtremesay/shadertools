import os

import moderngl_window as mglw


class ShaderViewer(mglw.WindowConfig):
    title = "Resource Loading with ModernGL Window"
    resizable = False
    gl_version = (3, 3)
    window_size = (800, 800)
    aspect_ratio = 1.0
    resource_dir = os.path.normpath(os.path.join(__file__, "../../../data"))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.program = self.load_program(
            vertex_shader="shaders/main.vs",
            fragment_shader="shaders/main.fs",
        )

        self.texture = self.load_texture_2d("colormaps/fractal.png")
        self.sampler = self.ctx.sampler(texture=self.texture)
        self.vao = self.ctx.vertex_array(self.program, [])
        self.vao.vertices = 3
        self.frame = 0

    def on_render(self, time, frame_time):
        print(time, frame_time)
        self.ctx.clear()
        self.program["iResolution"] = [self.window_size[0], self.window_size[1], 0.0]
        self.program["iTime"] = time

        # Theses uniforms are optional in the shader, and may not be present
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

        self.sampler.use()
        self.vao.render()
        self.frame += 1


def main():
    ShaderViewer.run()
