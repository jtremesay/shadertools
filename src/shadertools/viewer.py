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

from pathlib import Path
from typing import Optional

from .math import Vec2
from .window import Window


class ShaderViewer(Window):
    title = "Resource Loading with ModernGL Window"

    def __init__(self, shader: str, **kwargs):
        super().__init__(**kwargs)
        self.program = self.ctx.program(
            vertex_shader=(Path(self.resource_dir) / "shaders" / "main.vs").read_text(),
            fragment_shader=shader,
        )
        self.vao = self.ctx.vertex_array(self.program, [])
        self.vao.vertices = 3
        self.frame = 0

        self.mouse_click_start: Optional[Vec2] = None
        self.mouse_click_current: Optional[Vec2] = None

    def on_mouse_press_event(self, x, y, button):
        if button == 1:  # Left mouse button
            self.mouse_click_start = Vec2(x, y)
            self.mouse_click_current = self.mouse_click_start

        return super().on_mouse_press_event(x, y, button)

    def on_mouse_release_event(self, x, y, button):
        if button == 1:  # Left mouse button
            self.mouse_click_start = None
            self.mouse_click_current = None

        return super().on_mouse_release_event(x, y, button)

    def on_mouse_drag_event(self, x, y, dx, dy):
        if self.mouse_click_start is not None:
            self.mouse_click_current = Vec2(x, y)

        return super().on_mouse_drag_event(x, y, dx, dy)

    def on_render(self, time, frame_time):
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
            self.program["iMouse"] = (
                (
                    self.mouse_click_current.x,
                    self.mouse_click_current.y,
                    self.mouse_click_start.x,
                    self.mouse_click_start.y,
                )
                if self.mouse_click_current and self.mouse_click_start
                else (0.0, 0.0, 0.0, 0.0)
            )
        except KeyError:
            pass

        self.vao.render()
        self.frame += 1
