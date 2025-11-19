from shadertools.camera import Camera
from shadertools.math import Vec3


class TestCamera:
    def test_default_camera(self):
        camera = Camera()
        assert camera.position == Vec3(0, 0, 0)
        assert camera.view_port == Vec3(1, 1, 1)

    def test_custom_camera(self):
        camera = Camera(position=Vec3(1, 2, 3), view_port=Vec3(4, 5, 6))
        assert camera.position == Vec3(1, 2, 3)
        assert camera.view_port == Vec3(4, 5, 6)
