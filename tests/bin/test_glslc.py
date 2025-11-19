import pytest

from shadertools.bin.glslc import main


class TestGLSLC:
    def test_glslc_runs_without_errors(
        self, tmp_path: pytest.TempPathFactory, scene_path, ref_glsl_shader: str
    ):
        shader_path = tmp_path / "output.fs"

        main(["-o", str(shader_path), str(scene_path)])
        assert shader_path.exists()

        shader = shader_path.read_text()
        assert shader == ref_glsl_shader
