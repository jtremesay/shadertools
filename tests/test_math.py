from shadertools.math import Vec2, Vec3


class TestVec2:
    def test_default_constructor(self):
        v = Vec2()
        assert v.x == 0.0
        assert v.y == 0.0

    def test_parameterized_constructor(self):
        v = Vec2(1.0, 2.0)
        assert v.x == 1.0
        assert v.y == 2.0


class TestVec3:
    def test_default_constructor(self):
        v = Vec3()
        assert v.x == 0.0
        assert v.y == 0.0
        assert v.z == 0.0

    def test_parameterized_constructor(self):
        v = Vec3(1.0, 2.0, 3.0)
        assert v.x == 1.0
        assert v.y == 2.0
        assert v.z == 3.0
