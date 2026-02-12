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
"""Mathematical primitives for 3D graphics.

This module provides vector classes used throughout shadertools for representing
positions, directions, colors, and other 3D quantities.

Example:
    >>> position = Vec3(1.0, 2.0, 3.0)
    >>> color = Vec3(0.8, 0.2, 0.1)  # RGB color
    >>> uv = Vec2(0.5, 0.5)  # Texture coordinates
"""

from dataclasses import dataclass


@dataclass
class Vec2:
    """A 2D vector with x and y components.

    Used for 2D positions, texture coordinates, or any 2D quantity.

    Attributes:
        x: The x component (default: 0.0).
        y: The y component (default: 0.0).

    Example:
        >>> uv = Vec2(0.5, 0.75)
        >>> origin = Vec2()  # Defaults to (0.0, 0.0)
    """

    x: float = 0.0
    y: float = 0.0


@dataclass
class Vec3(Vec2):
    """A 3D vector extending Vec2 with a z component.

    Used for 3D positions, directions, colors (RGB), and other 3D quantities.
    Inherits x and y from Vec2.

    Attributes:
        x: The x component (inherited from Vec2, default: 0.0).
        y: The y component (inherited from Vec2, default: 0.0).
        z: The z component (default: 0.0).

    Example:
        >>> position = Vec3(1.0, 2.0, 3.0)
        >>> red = Vec3(1.0, 0.0, 0.0)  # Red color
        >>> origin = Vec3()  # Defaults to (0.0, 0.0, 0.0)
    """

    z: float = 0.0
