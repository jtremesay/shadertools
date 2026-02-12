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
"""Window management and event handling for shader applications.

This module provides the Window base class that wraps moderngl-window functionality,
handling window creation, OpenGL context management, and event processing.

Example:
    >>> window = Window()
    >>> window.run()  # Start the main event loop
"""

import os
import random

import moderngl_window
from moderngl_window.conf import settings
from moderngl_window.timers.clock import Timer


class Window:
    """Base window class for OpenGL applications.

    Provides a customizable window with OpenGL context and event handling.
    Wraps moderngl-window to create the window, manage the main loop, and
    register event callbacks.

    This class is designed to be subclassed to create custom OpenGL applications.
    Override on_render() and event handler methods to implement custom behavior.

    Attributes:
        window_class: ModernGL window backend class to use.
        title: Window title displayed in the title bar.
        resizable: Whether the window can be resized by the user.
        gl_version: OpenGL version tuple (major, minor).
        window_size: Window dimensions as (width, height) in pixels.
        aspect_ratio: Window aspect ratio (width / height).
        resource_dir: Directory path for loading resources (shaders, etc.).
        wnd: The moderngl-window Window instance.
        ctx: The ModernGL context for rendering.

    Example:
        >>> # Using the base Window class
        >>> window = Window()
        >>> window.run()
        >>>
        >>> # Subclassing for custom behavior
        >>> class MyWindow(Window):
        ...     def on_render(self, time, frame_time):
        ...         self.ctx.clear(0.1, 0.1, 0.1, 1.0)
        >>> my_window = MyWindow()
        >>> my_window.run()
    """

    window_class = "moderngl_window.context.pyglet.Window"
    title = "ShaderTools Window"
    resizable = False
    gl_version = (3, 3)
    window_size = (512, 512)
    aspect_ratio = window_size[0] / window_size[1]
    resource_dir = os.path.normpath(os.path.join(__file__, "../data"))

    def __init__(self) -> None:
        """Initialize the window and OpenGL context.

        Creates a moderngl-window instance with the configured settings and
        registers all event handler methods.
        """
        # Configure to use pyglet window
        settings.WINDOW["class"] = self.window_class
        settings.WINDOW["title"] = self.title
        settings.WINDOW["resizable"] = self.resizable
        settings.WINDOW["gl_version"] = self.gl_version
        settings.WINDOW["size"] = self.window_size
        settings.WINDOW["aspect_ratio"] = self.aspect_ratio

        self.wnd = moderngl_window.create_window_from_settings()
        self.ctx = self.wnd.ctx

        # register event methods
        self.wnd.resize_func = self.on_resize
        self.wnd.iconify_func = self.on_iconify
        self.wnd.key_event_func = self.on_key_event
        self.wnd.mouse_position_event_func = self.on_mouse_position_event
        self.wnd.mouse_drag_event_func = self.on_mouse_drag_event
        self.wnd.mouse_scroll_event_func = self.on_mouse_scroll_event
        self.wnd.mouse_press_event_func = self.on_mouse_press_event
        self.wnd.mouse_release_event_func = self.on_mouse_release_event
        self.wnd.unicode_char_entered_func = self.on_unicode_char_entered
        self.wnd.close_func = self.on_close

    def on_render(self, time: float, frame_time: float) -> None:
        """Render the current frame.

        Override this method in subclasses to implement custom rendering logic.

        Args:
            time: Total elapsed time in seconds since the timer started.
            frame_time: Time elapsed since the previous frame in seconds.
        """
        pass

    def run(self) -> None:
        """Start the main event loop.

        Runs the window's main loop, calling on_render() for each frame until
        the window is closed. Handles timing and buffer swapping automatically.
        """
        timer = Timer()
        timer.start()

        while not self.wnd.is_closing:
            self.wnd.clear()
            time, frame_time = timer.next_frame()
            self.on_render(time, frame_time)
            self.wnd.swap_buffers()

        self.wnd.destroy()

    def on_resize(self, width: int, height: int) -> None:
        """Handle window resize events.

        Called when the window is resized by the user or system.

        Args:
            width: New window width in pixels.
            height: New window height in pixels.
        """
        print("Window was resized. buffer size is {} x {}".format(width, height))

    def on_iconify(self, iconify: bool) -> None:
        """Handle window iconify (minimize) events.

        Called when the window is minimized/hidden or restored.

        Args:
            iconify: True if window was iconified, False if restored.
        """
        print("Window was iconified:", iconify)

    def on_key_event(self, key: int, action: int, modifiers: object) -> None:
        """Handle keyboard events.

        Called for key press and release events. Default implementation provides
        example keyboard controls for window manipulation.

        Args:
            key: The key code that was pressed or released.
            action: The action type (ACTION_PRESS or ACTION_RELEASE).
            modifiers: Modifier keys state (shift, ctrl, alt, etc.).
        """
        keys = self.wnd.keys

        # Key presses
        if action == keys.ACTION_PRESS:
            if key == keys.SPACE:
                print("SPACE key was pressed")

            # Using modifiers (shift and ctrl)

            if key == keys.Z and modifiers.shift:
                print("Shift + Z was pressed")

            if key == keys.Z and modifiers.ctrl:
                print("ctrl + Z was pressed")

        # Key releases
        elif action == self.wnd.keys.ACTION_RELEASE:
            if key == keys.SPACE:
                print("SPACE key was released")

        # Move the window around with AWSD
        if action == keys.ACTION_PRESS:
            if key == keys.A:
                self.wnd.position = self.wnd.position[0] - 10, self.wnd.position[1]
            if key == keys.D:
                self.wnd.position = self.wnd.position[0] + 10, self.wnd.position[1]
            if key == keys.W:
                self.wnd.position = self.wnd.position[0], self.wnd.position[1] - 10
            if key == keys.S:
                self.wnd.position = self.wnd.position[0], self.wnd.position[1] + 10

            # toggle cursor
            if key == keys.C:
                self.wnd.cursor = not self.wnd.cursor

            # Shuffle window tittle
            if key == keys.T:
                title = list(self.wnd.title)
                random.shuffle(title)
                self.wnd.title = "".join(title)

            # Toggle mouse exclusivity
            if key == keys.M:
                self.wnd.mouse_exclusivity = not self.wnd.mouse_exclusivity

    def on_mouse_position_event(self, x: int, y: int, dx: int, dy: int) -> None:
        """Handle mouse movement events.

        Called when the mouse cursor moves within the window.

        Args:
            x: Current mouse x position in pixels.
            y: Current mouse y position in pixels.
            dx: Change in x position since last event.
            dy: Change in y position since last event.
        """
        print("Mouse position pos={} {} delta={} {}".format(x, y, dx, dy))

    def on_mouse_drag_event(self, x: int, y: int, dx: int, dy: int) -> None:
        """Handle mouse drag events.

        Called when the mouse is moved while a button is pressed.

        Args:
            x: Current mouse x position in pixels.
            y: Current mouse y position in pixels.
            dx: Change in x position since last event.
            dy: Change in y position since last event.
        """
        print("Mouse drag pos={} {} delta={} {}".format(x, y, dx, dy))

    def on_mouse_scroll_event(self, x_offset: float, y_offset: float) -> None:
        """Handle mouse scroll wheel events.

        Called when the mouse scroll wheel is moved.

        Args:
            x_offset: Horizontal scroll offset.
            y_offset: Vertical scroll offset (positive = scroll up).
        """
        print("mouse_scroll_event", x_offset, y_offset)

    def on_mouse_press_event(self, x: int, y: int, button: int) -> None:
        """Handle mouse button press events.

        Called when a mouse button is pressed.

        Args:
            x: Mouse x position in pixels when button was pressed.
            y: Mouse y position in pixels when button was pressed.
            button: The button number that was pressed (1=left, 2=right, etc.).
        """
        print("Mouse button {} pressed at {}, {}".format(button, x, y))
        print("Mouse states:", self.wnd.mouse_states)

    def on_mouse_release_event(self, x: int, y: int, button: int) -> None:
        """Handle mouse button release events.

        Called when a mouse button is released.

        Args:
            x: Mouse x position in pixels when button was released.
            y: Mouse y position in pixels when button was released.
            button: The button number that was released (1=left, 2=right, etc.).
        """
        print("Mouse button {} released at {}, {}".format(button, x, y))
        print("Mouse states:", self.wnd.mouse_states)

    def on_unicode_char_entered(self, char: str) -> None:
        """Handle unicode character input events.

        Called when a unicode character is entered (text input).

        Args:
            char: The unicode character that was entered.
        """
        print("unicode_char_entered:", char)

    def on_close(self) -> None:
        """Handle window close events.

        Called when the window is about to close.
        """
        print("Window was closed")
