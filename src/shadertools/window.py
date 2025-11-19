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
import random

import moderngl_window
from moderngl_window.conf import settings
from moderngl_window.timers.clock import Timer


class Window:
    """
    Custom setup using a class.
    We create the window, main loop and register events.
    """

    window_class = "moderngl_window.context.pyglet.Window"
    title = "ShaderTools Window"
    resizable = False
    gl_version = (3, 3)
    window_size = (512, 512)
    aspect_ratio = window_size[0] / window_size[1]
    resource_dir = os.path.normpath(os.path.join(__file__, "../data"))

    def __init__(self):
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

    def on_render(self, time, frame_time):
        pass

    def run(self):
        timer = Timer()
        timer.start()

        while not self.wnd.is_closing:
            self.wnd.clear()
            time, frame_time = timer.next_frame()
            self.on_render(time, frame_time)
            self.wnd.swap_buffers()

        self.wnd.destroy()

    def on_resize(self, width: int, height: int):
        print("Window was resized. buffer size is {} x {}".format(width, height))

    def on_iconify(self, iconify: bool):
        """Window hide/minimize and restore"""
        print("Window was iconified:", iconify)

    def on_key_event(self, key, action, modifiers):
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

    def on_mouse_position_event(self, x, y, dx, dy):
        print("Mouse position pos={} {} delta={} {}".format(x, y, dx, dy))

    def on_mouse_drag_event(self, x, y, dx, dy):
        print("Mouse drag pos={} {} delta={} {}".format(x, y, dx, dy))

    def on_mouse_scroll_event(self, x_offset, y_offset):
        print("mouse_scroll_event", x_offset, y_offset)

    def on_mouse_press_event(self, x, y, button):
        print("Mouse button {} pressed at {}, {}".format(button, x, y))
        print("Mouse states:", self.wnd.mouse_states)

    def on_mouse_release_event(self, x: int, y: int, button: int):
        print("Mouse button {} released at {}, {}".format(button, x, y))
        print("Mouse states:", self.wnd.mouse_states)

    def on_unicode_char_entered(self, char):
        print("unicode_char_entered:", char)

    def on_close(self):
        print("Window was closed")
