from shadertools.geometry import Sphere
from shadertools.material import Material
from shadertools.math import Vec3
from shadertools.scene import Scene


class TestScene:
    def test_scene_initialization(self):
        scene = Scene()
        assert scene.spheres == []
        assert scene.camera.position == Vec3(0, 0, 0)

    def test_adding_spheres(self):
        scene = Scene()
        sphere1 = Sphere(
            center=Vec3(1, 2, 3), radius=1.0, material=Material(color=Vec3(1, 0, 0))
        )
        sphere2 = Sphere(
            center=Vec3(4, 5, 6), radius=2.0, material=Material(color=Vec3(0, 1, 0))
        )
        scene.spheres.append(sphere1)
        scene.spheres.append(sphere2)
        assert len(scene.spheres) == 2
        assert scene.spheres[0] == sphere1
        assert scene.spheres[1] == sphere2
