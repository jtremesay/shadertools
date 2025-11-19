from pathlib import Path

import pytest

from shadertools.loaders import load_scene
from shadertools.scene import Scene

TESTS_DATA = Path("tests/data")
SCENE_PATH = TESTS_DATA / "scene.py"
REF_ST_SHADER_PATH = TESTS_DATA / "scene.st.fs"
REF_GLSL_SHADER_PATH = TESTS_DATA / "scene.fs"


@pytest.fixture(autouse=True)
def scene_path() -> Path:
    return SCENE_PATH


@pytest.fixture(autouse=True)
def scene() -> Scene:
    return load_scene(SCENE_PATH)


@pytest.fixture(autouse=True)
def ref_st_shader() -> str:
    return REF_ST_SHADER_PATH.read_text().strip()


@pytest.fixture(autouse=True)
def ref_glsl_shader() -> str:
    return REF_GLSL_SHADER_PATH.read_text().strip()
