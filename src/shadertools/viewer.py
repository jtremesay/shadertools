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
"""Interactive shader viewer with Shadertoy-compatible uniform support.

This module provides the ShaderViewer class for displaying and interacting with
compiled shaders. It extends the Window class with shader-specific rendering
and mouse interaction tracking.

Example:
    >>> from shadertools.compiler import compile_scene_to_glsl_shader
    >>> scene = Scene(...)  # Your scene
    >>> shader_code = compile_scene_to_glsl_shader(scene)
    >>> viewer = ShaderViewer(shader_code)
    >>> viewer.run()
"""

from pathlib import Path
from typing import Any, Optional

from .hll.math import Vec2
from .window import Window


class ShaderViewer(Window):
    """Interactive viewer for fragment shaders.

    Displays a shader in full-screen quad and provides Shadertoy-compatible
    uniform variables (iTime, iResolution, iMouse, etc.). Tracks mouse
    interactions for shader interactivity.

    The viewer automatically sets standard Shadertoy uniforms if they exist
    in the shader:
        - iResolution: Window resolution (vec3)
        - iTime: Elapsed time in seconds (float)
        - iTimeDelta: Frame time in seconds (float)
        - iFrameRate: Frames per second (float)
        - iFrame: Current frame number (int)
        - iMouse: Mouse position and click state (vec4)

    Attributes:
        title: Window title.
        program: The compiled shader program.
        vao: Vertex array object for rendering the full-screen quad.
        frame: Current frame number.
        mouse_click_start: Position where left mouse button was pressed, or None.
        mouse_click_current: Current mouse drag position, or None.

    Example:
        >>> shader_code = '''  # Your GLSL fragment shader
        ... #version 330
        ... uniform vec3 iResolution;
        ... uniform float iTime;
        ... out vec4 fragColor;
        ... void main() {
        ...     vec2 uv = gl_FragCoord.xy / iResolution.xy;
        ...     fragColor = vec4(uv, 0.5 + 0.5 * sin(iTime), 1.0);
        ... }
        ... '''
        >>> viewer = ShaderViewer(shader_code)
        >>> viewer.run()
    """

    title = "ShaderTools Viewer"

    def __init__(self, shader: str, **kwargs: Any) -> None:
        """Initialize the shader viewer.

        Args:
            shader: GLSL fragment shader source code as a string.
            **kwargs: Additional keyword arguments passed to the Window constructor.
        """
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

    def on_mouse_press_event(self, x: int, y: int, button: int) -> None:
        """Handle mouse button press events.

        Tracks left mouse button clicks for the iMouse uniform.

        Args:
            x: Mouse x position in pixels when button was pressed.
            y: Mouse y position in pixels when button was pressed.
            button: The button number that was pressed (1=left, 2=right, etc.).
        """
        if button == 1:  # Left mouse button
            self.mouse_click_start = Vec2(x, y)
            self.mouse_click_current = self.mouse_click_start

        return super().on_mouse_press_event(x, y, button)

    def on_mouse_release_event(self, x: int, y: int, button: int) -> None:
        """Handle mouse button release events.

        Clears mouse tracking when left button is released.

        Args:
            x: Mouse x position in pixels when button was released.
            y: Mouse y position in pixels when button was released.
            button: The button number that was released (1=left, 2=right, etc.).
        """
        if button == 1:  # Left mouse button
            self.mouse_click_start = None
            self.mouse_click_current = None

        return super().on_mouse_release_event(x, y, button)

    def on_mouse_drag_event(self, x: int, y: int, dx: int, dy: int) -> None:
        """Handle mouse drag events.

        Updates the current mouse position for the iMouse uniform during drag.

        Args:
            x: Current mouse x position in pixels.
            y: Current mouse y position in pixels.
            dx: Change in x position since last event.
            dy: Change in y position since last event.
        """
        if self.mouse_click_start is not None:
            self.mouse_click_current = Vec2(x, y)

        return super().on_mouse_drag_event(x, y, dx, dy)

    def on_render(self, time: float, frame_time: float) -> None:
        """Render the shader for the current frame.

        Clears the screen, sets Shadertoy-compatible uniforms (if present in the
        shader), and renders the full-screen quad with the shader applied.

        Args:
            time: Total elapsed time in seconds since the timer started.
            frame_time: Time elapsed since the previous frame in seconds.
        """
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
