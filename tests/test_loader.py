from pathlib import Path

import pytest

from shadertools.loaders import load_scene


class TestLoadScene:
    def test_load_scene(self, tmp_path):
        # Create a temporary scene file
        scene = load_scene(Path("tests/data/scene.py"))
        assert scene is not None
        assert len(scene.spheres) == 3
        assert scene.spheres[0].material.color.x == 1
        assert scene.spheres[1].material.color.y == 1
        assert scene.spheres[2].material.color.z == 1

    def test_load_nonexistent_scene(self):
        with pytest.raises(FileNotFoundError) as e:
            load_scene(Path("nonexistent_scene.py"))
