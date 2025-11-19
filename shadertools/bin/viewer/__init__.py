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
            vertex_shader="shaders/fractal.vs",
            fragment_shader="shaders/fractal.fs",
        )

        self.texture = self.load_texture_2d("colormaps/fractal.png")
        self.sampler = self.ctx.sampler(texture=self.texture)
        self.vao = self.ctx.vertex_array(self.program, [])
        self.vao.vertices = 3

    def on_render(self, time, frame_time):
        self.ctx.clear()
        self.program["seed"] = (-0.8, 0.156)
        self.program["iter"] = 100
        self.sampler.use()
        self.vao.render()


def main():
    ShaderViewer.run()
