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
"""Scene loading utilities.

This module provides functionality to load scene definitions from Python files.
Scene files should define a `create_scene()` function that returns a Scene object.
"""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from .scene import Scene


def load_scene(path: Path) -> Scene:
    """Load a scene from a Python file.

    Dynamically imports a Python module from the given path and calls its
    `create_scene()` function to obtain a Scene object.

    Args:
        path: Path to a Python file containing a `create_scene()` function.

    Returns:
        A Scene object returned by the module's `create_scene()` function.

    Raises:
        AssertionError: If the module cannot be loaded from the given path.
        AttributeError: If the module doesn't have a `create_scene()` function.

    Example:
        >>> from pathlib import Path
        >>> scene = load_scene(Path("my_scene.py"))
        >>> # The scene.py file should contain:
        >>> # def create_scene():
        >>> #     return Scene(...)
    """
    scene_module_name = path.stem
    spec = spec_from_file_location(scene_module_name, path)
    assert spec is not None and spec.loader is not None, (
        f"Could not load module from {path}"
    )
    scene_module = module_from_spec(spec)
    spec.loader.exec_module(scene_module)

    # Create the scene and compile the shader
    return scene_module.create_scene()
