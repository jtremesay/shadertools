import sys
from pathlib import Path

from shadertools.compiler import (
    compile_scene_to_shadertoy_shader,
    compile_shadertoy_shader_to_glsl_shader,
)
from shadertools.scene import Camera, Material, Scene, SdfUnion, Sphere
from shadertools.viewer import ShaderViewer

scene = Scene(
    camera=Camera(),
    root=SdfUnion(
        nodes=[
            Sphere(center=(0, -1, 3), radius=1, material=Material(color=(1, 0, 0))),
            Sphere(center=(2, 0, 4), radius=1, material=Material(color=(0, 1, 0))),
            Sphere(center=(-2, 0, 4), radius=1, material=Material(color=(0, 0, 1))),
        ]
    ),
)

print(scene)
shadertoy_shader = compile_scene_to_shadertoy_shader(scene)
Path("output_shadertoy_shader.fs").write_text(shadertoy_shader)

glsl_shader = compile_shadertoy_shader_to_glsl_shader(shadertoy_shader)
Path("output_glsl_shader.fs").write_text(glsl_shader)

sys.argv.append("--shader-file=output_glsl_shader.fs")
ShaderViewer.run()
