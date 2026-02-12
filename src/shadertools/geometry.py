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
"""Geometric primitives for 3D scenes.

This module defines geometric shapes that can be rendered using signed distance
functions (SDFs). All geometry inherits from the Node base class.
"""

from dataclasses import dataclass

from .material import Material
from .math import Vec3


@dataclass
class Node:
    """Base class for all geometric nodes in a scene.

    This is an abstract base class that all geometric primitives inherit from.
    Currently serves as a marker class for type hierarchy.
    """

    pass


@dataclass
class Sphere(Node):
    """A sphere primitive defined by center position and radius.

    Spheres are rendered using signed distance functions (SDFs) in the shader.

    Attributes:
        center: The 3D position of the sphere's center point.
        radius: The radius of the sphere (must be positive).
        material: The material properties defining the sphere's appearance.

    Example:
        >>> from shadertools.math import Vec3
        >>> from shadertools.material import Material
        >>>
        >>> mat = Material(color=Vec3(1.0, 0.0, 0.0), specular=0.8)
        >>> sphere = Sphere(center=Vec3(0, 0, -5), radius=1.5, material=mat)
    """

    center: Vec3
    radius: float
    material: Material
