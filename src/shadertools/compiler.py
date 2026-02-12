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
"""Shader compilation from scene descriptions to GLSL and Shadertoy formats.

This module provides the core compilation functionality that transforms Scene objects
into executable shader code. It uses Jinja2 templates to generate shaders for different
target platforms (GLSL, Shadertoy).

The compilation process:
    1. Takes a Scene object with geometric primitives and camera
    2. Renders it through Jinja2 templates with custom filters
    3. Produces shader code with SDF (signed distance function) rendering

Example:
    >>> from shadertools.scene import Scene
    >>> from shadertools.compiler import compile_scene_to_glsl_shader
    >>>
    >>> scene = Scene(...)  # Create your scene
    >>> shader_code = compile_scene_to_glsl_shader(scene)
"""

from jinja2 import Environment, PackageLoader

from .math import Vec3
from .scene import Scene

env = Environment(loader=PackageLoader("shadertools"))


def glsl_vec3(v: Vec3) -> str:
    """Convert a Vec3 to GLSL vec3 constructor syntax.

    This is a Jinja2 template filter that transforms Python Vec3 objects into
    valid GLSL code for vec3 constructors.

    Args:
        v: The Vec3 to convert.

    Returns:
        A string containing GLSL vec3 constructor, e.g., "vec3(1.0, 2.0, 3.0)".

    Example:
        >>> from shadertools.math import Vec3
        >>> glsl_vec3(Vec3(1.0, 0.5, 0.0))
        'vec3(1.0, 0.5, 0.0)'
    """
    return f"vec3({v.x}, {v.y}, {v.z})"


env.filters["glsl_vec3"] = glsl_vec3


def compile_scene_to_shadertoy_shader(scene: Scene) -> str:
    """Compile a Scene to Shadertoy-compatible GLSL shader code.

    Generates a complete shader that can be pasted directly into Shadertoy.com.
    The shader implements raymarching with signed distance functions (SDFs) for
    all scene objects.

    Args:
        scene: The Scene object to compile.

    Returns:
        Complete Shadertoy shader code as a string.

    Example:
        >>> scene = Scene(...)  # Your scene definition
        >>> shader = compile_scene_to_shadertoy_shader(scene)
        >>> # Copy shader to Shadertoy.com
    """
    tpl = env.get_template("shaders/st.fs")
    return tpl.render(scene=scene)


def compile_scene_to_glsl_shader(scene: Scene) -> str:
    """Compile a Scene to standalone GLSL fragment shader code.

    Generates a GLSL fragment shader suitable for use with OpenGL applications.
    The shader implements raymarching with signed distance functions (SDFs) for
    all scene objects.

    Args:
        scene: The Scene object to compile.

    Returns:
        Complete GLSL fragment shader code as a string.

    Example:
        >>> scene = Scene(...)  # Your scene definition
        >>> shader = compile_scene_to_glsl_shader(scene)
        >>> # Use shader with OpenGL/ModernGL
    """
    tpl = env.get_template("shaders/glsl.fs")
    return tpl.render(scene=scene)
