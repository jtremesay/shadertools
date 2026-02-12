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
"""Scene composition and management.

This module defines the Scene class which aggregates all elements needed to render
a 3D scene, including geometric objects and camera configuration.
"""

from dataclasses import dataclass, field

from .camera import Camera
from .geometry import Sphere


@dataclass
class Scene:
    """A complete 3D scene containing objects and a camera.

    The Scene class serves as a container for all renderable elements and view
    configuration. Scenes can be compiled to GLSL or Shadertoy shaders for rendering.

    Attributes:
        spheres: List of Sphere objects in the scene. Defaults to empty list.
        camera: Camera configuration for rendering the scene. Defaults to a
            camera at the origin.

    Example:
        >>> from shadertools.math import Vec3
        >>> from shadertools.material import Material
        >>> from shadertools.geometry import Sphere
        >>> from shadertools.camera import Camera
        >>>
        >>> # Create materials
        >>> red_mat = Material(color=Vec3(1.0, 0.0, 0.0), specular=0.8)
        >>> blue_mat = Material(color=Vec3(0.0, 0.2, 0.8), specular=0.5)
        >>>
        >>> # Create spheres
        >>> sphere1 = Sphere(center=Vec3(-2, 0, -5), radius=1.0, material=red_mat)
        >>> sphere2 = Sphere(center=Vec3(2, 0, -5), radius=1.5, material=blue_mat)
        >>>
        >>> # Create scene
        >>> scene = Scene(
        ...     spheres=[sphere1, sphere2],
        ...     camera=Camera(position=Vec3(0, 1, 0))
        ... )
    """

    spheres: list[Sphere] = field(default_factory=list)
    camera: Camera = field(default_factory=Camera)
