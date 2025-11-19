# ANTI-CAPITALIST SOFTWARE LICENSE (v 1.4)
#
# Copyright © 2025 Jonathan Tremesayques
#
# This is anti-capitalist software, released for free use by individuals and
# organizations that do not operate by capitalist principles.
#
# Permission is hereby granted, free of charge, to any person or organization
# (the "User") obtaining a copy of this software and associated documentation
# files (the "Software"), to use, copy, modify, merge, distribute, and/or sell
# copies of the Software, subject to the following conditions:
#
#   1. The above copyright notice and this permission notice shall be included
#      in all copies or modified versions of the Software.
#
#   2. The User is one of the following:
#     a. An individual person, laboring for themselves
#     b. A non-profit organization
#     c. An educational institution
#     d. An organization that seeks shared profit for all of its members, and
#        allows non-members to set the cost of their labor
#
#   3. If the User is an organization with owners, then all owners are workers
#     and all workers are owners with equal equity and/or equal vote.
#
#   4. If the User is an organization, then the User is not law enforcement or
#      military, or working for or under either.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT EXPRESS OR IMPLIED WARRANTY OF ANY
# KIND, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
