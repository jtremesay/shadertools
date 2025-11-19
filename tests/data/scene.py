from shadertools.camera import Camera
from shadertools.geometry import Sphere
from shadertools.material import Material
from shadertools.math import Vec3
from shadertools.scene import Scene


def create_scene() -> Scene:
    return Scene(
        camera=Camera(),
        spheres=[
            Sphere(
                center=Vec3(0, -1, 3),
                radius=1,
                material=Material(color=Vec3(1, 0, 0)),
            ),
            Sphere(
                center=Vec3(3, 0, 4),
                radius=1,
                material=Material(color=Vec3(0, 1, 0)),
            ),
            Sphere(
                center=Vec3(-2, 0, 4),
                radius=1,
                material=Material(color=Vec3(0, 0, 1)),
            ),
        ],
    )
