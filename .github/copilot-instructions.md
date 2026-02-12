# GitHub Copilot Instructions for ShaderTools

## Project Overview

ShaderTools is a Python library for creating 3D scenes and compiling them into GLSL or Shadertoy-compatible fragment shaders using signed distance functions (SDFs).

## Code Style & Standards

### Python Version
- Target Python 3.13+
- Use modern Python features where appropriate

### Type Annotations
- **Always** include type hints for all function parameters and return values
- Use `from typing import Optional, Any` etc. where needed
- Use modern type syntax: `list[str]` not `List[str]`, `dict[str, int]` not `Dict[str, int]`
- Use `from collections.abc import Sequence` for flexible sequence types

### Documentation
- **All modules** must have a module-level docstring
- **All classes** must have a class docstring
- **All public functions/methods** must have docstrings
- Use **Google-style docstrings** consistently:
  ```python
  def function(param1: str, param2: int) -> bool:
      """Brief description.

      Longer description if needed.

      Args:
          param1: Description of param1.
          param2: Description of param2.

      Returns:
          Description of return value.

      Example:
          >>> function("test", 42)
          True
      """
  ```
- Include usage examples in module and class docstrings where helpful

### Data Classes
- Prefer `@dataclass` for data structures
- Use `field(default_factory=...)` for mutable defaults
- Always include type annotations on dataclass fields
- Add class docstrings explaining purpose and usage

### Imports
- Organize imports: standard library, third-party, local imports
- Use absolute imports within the package: `from .math import Vec3`

## Architecture & Patterns

### Core Concepts
- **Vec2/Vec3**: Basic vector math primitives
- **Material**: Visual appearance properties (color, specular)
- **Geometry**: SDF-based primitives (Sphere, etc.) inheriting from Node base class
- **Scene**: Container for geometry and camera
- **Compiler**: Jinja2-based shader generation
- **Viewer**: Interactive OpenGL window with Shadertoy-compatible uniforms

### Shader Generation
- Use Jinja2 templates in `src/shadertools/templates/`
- Custom filters like `glsl_vec3` for converting Python objects to GLSL syntax
- Support both GLSL and Shadertoy output formats

### Event Handling
- Window and viewer use event handler methods: `on_render`, `on_key_event`, `on_mouse_*`
- Always include type hints for event handler parameters
- Event handlers should call `super()` when appropriate

## License Header

All new Python files must include the ANTI-CAPITALIST SOFTWARE LICENSE header:

```python
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
```

## Dependencies

### Required Packages
- **jinja2**: Template engine for shader code generation
- **moderngl-window**: OpenGL window management and context creation

### Key External APIs
- **moderngl_window**: Window creation, event handling, OpenGL context
- **Jinja2**: Template loading, rendering, custom filters

## Testing & CLI

### Command-Line Tools
- `glslc`: Compile scenes to GLSL shaders
- `stc`: Compile scenes to Shadertoy shaders
- `viewer`: Interactive scene viewer

### CLI Function Signature
- CLI `main()` functions use `Optional[Sequence[str]]` for testability
- Always include helpful argparse descriptions and help text

## Common Patterns

### Scene Files
Scene files should define a `create_scene()` function returning a Scene object:

```python
def create_scene() -> Scene:
    return Scene(
        spheres=[...],
        camera=Camera(...)
    )
```

### Adding New Geometry Primitives
1. Inherit from `Node` base class
2. Use `@dataclass` decorator
3. Include center/position, dimensions, and material
4. Update compiler templates to handle new primitive

### Shadertoy Uniforms
The viewer automatically provides these uniforms if present in shaders:
- `iResolution` (vec3): Window resolution
- `iTime` (float): Elapsed time
- `iTimeDelta` (float): Frame time
- `iFrame` (int): Frame number
- `iMouse` (vec4): Mouse position and click state

## Best Practices

1. **Explicit over implicit**: Use clear variable names and explicit type hints
2. **Consistent formatting**: Follow existing code style
3. **Documentation first**: Write docstrings as you code, not after
4. **Type safety**: Leverage type hints for better IDE support and error catching
5. **Examples in docs**: Include usage examples in docstrings for complex APIs
6. **Error messages**: Provide helpful assertion messages and error descriptions
