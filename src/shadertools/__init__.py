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
"""ShaderTools: A toolkit for creating and rendering 3D scenes with GLSL shaders.

ShaderTools is a Python library that provides a high-level interface for creating
3D scenes and compiling them into GLSL or Shadertoy-compatible fragment shaders.
It uses signed distance functions (SDFs) for rendering geometric primitives and
supports real-time interactive viewing.

Architecture
------------
The library is organized into several modules:

    - **math**: Vector primitives (Vec2, Vec3) for 3D graphics
    - **material**: Material properties (color, specular) for object appearance
    - **geometry**: Geometric primitives (Sphere, etc.) using SDFs
    - **camera**: Camera configuration for scene rendering
    - **scene**: Scene composition combining geometry and camera
    - **compiler**: Jinja2-based shader compilation to GLSL/Shadertoy
    - **loaders**: Dynamic scene loading from Python files
    - **window**: OpenGL window management and event handling
    - **viewer**: Interactive shader viewer with Shadertoy-compatible uniforms
    - **bin**: Command-line tools (glslc, stc, viewer)

Workflow
--------
1. **Define a scene** with geometric primitives, materials, and camera
2. **Compile** the scene to GLSL or Shadertoy shader code
3. **View** the shader interactively or save it to a file

Basic Usage Example
-------------------
>>> from shadertools.math import Vec3
>>> from shadertools.material import Material
>>> from shadertools.geometry import Sphere
>>> from shadertools.camera import Camera
>>> from shadertools.scene import Scene
>>> from shadertools.compiler import compile_scene_to_glsl_shader
>>> from shadertools.viewer import ShaderViewer
>>>
>>> # Create materials
>>> red_mat = Material(color=Vec3(1.0, 0.0, 0.0), specular=0.8)
>>> blue_mat = Material(color=Vec3(0.0, 0.2, 0.8), specular=0.5)
>>>
>>> # Create scene with spheres
>>> scene = Scene(
...     spheres=[
...         Sphere(center=Vec3(-2, 0, -5), radius=1.0, material=red_mat),
...         Sphere(center=Vec3(2, 0, -5), radius=1.5, material=blue_mat),
...     ],
...     camera=Camera(position=Vec3(0, 1, 0))
... )
>>>
>>> # Compile and view
>>> shader = compile_scene_to_glsl_shader(scene)
>>> viewer = ShaderViewer(shader)
>>> viewer.run()  # Opens interactive window

Scene File Workflow
--------------------
Create a scene description file (e.g., my_scene.py):

.. code-block:: python

    from shadertools.math import Vec3
    from shadertools.material import Material
    from shadertools.geometry import Sphere
    from shadertools.camera import Camera
    from shadertools.scene import Scene

    def create_scene():
        return Scene(
            spheres=[
                Sphere(
                    center=Vec3(0, 0, -5),
                    radius=1.5,
                    material=Material(color=Vec3(1.0, 0.2, 0.1), specular=0.9)
                )
            ],
            camera=Camera()
        )

Then use the CLI tools:

.. code-block:: bash

    # View interactively
    python -m shadertools.bin.viewer my_scene.py

    # Compile to GLSL
    python -m shadertools.bin.glslc my_scene.py -o output.fs

    # Compile to Shadertoy
    python -m shadertools.bin.stc my_scene.py -o shadertoy.fs

Requirements
------------
- Python >= 3.13
- jinja2: Template engine for shader generation
- moderngl-window: OpenGL context and window management

See Also
--------
- Shadertoy: https://www.shadertoy.com/
- Signed Distance Functions: https://iquilezles.org/articles/distfunctions/
"""
