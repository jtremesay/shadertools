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
"""Interactive shader viewer CLI.

Command-line tool for viewing and interacting with ShaderTools scene files
in real-time using an OpenGL window.
"""

from argparse import ArgumentParser
from collections.abc import Sequence
from pathlib import Path
from typing import Optional

from ...compiler import compile_scene_to_glsl_shader
from ...loaders import load_scene
from ...viewer import ShaderViewer


def main(args: Optional[Sequence[str]] = None) -> None:
    """Launch interactive viewer for a scene file.

    Command-line interface for viewing ShaderTools scenes in an interactive
    OpenGL window. The viewer provides real-time rendering with mouse interaction.

    Args:
        args: Command-line arguments to parse. If None (default), uses sys.argv.

    Example:
        From command line:
            $ python -m shadertools.bin.viewer scene.py
            $ python -m shadertools.bin.viewer --help

        From Python:
            >>> from shadertools.bin.viewer import main
            >>> main(["scene.py"])  # Opens interactive viewer window
    """
    parser = ArgumentParser(description="ShaderTools Viewer")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "scene",
        type=Path,
        nargs="?",
        default=Path("scene.py"),
        help="Scene file to load",
    )
    parsed_args = parser.parse_args(args)
    scene = load_scene(parsed_args.scene)
    shader = compile_scene_to_glsl_shader(scene)
    ShaderViewer(shader).run()
