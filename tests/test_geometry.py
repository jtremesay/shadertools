from shadertools.geometry import Sphere
from shadertools.material import Material
from shadertools.math import Vec3


class TestSphere:
    def test_sphere_creation(self):
        center = Vec3(0.0, 0.0, 0.0)
        radius = 1.0
        material = Material(color=Vec3(1.0, 0.0, 0.0))
        sphere = Sphere(center=center, radius=radius, material=material)

        assert isinstance(sphere, Sphere)
        assert sphere.center == center
        assert sphere.radius == radius
        assert sphere.material == material
