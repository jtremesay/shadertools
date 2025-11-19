import pytest

from shadertools.bin.stc import main


class TestSTC:
    def test_stc_runs_without_errors(
        self, tmp_path: pytest.TempPathFactory, scene_path, ref_st_shader: str
    ):
        st_shader_path = tmp_path / "output.st.fs"

        main(["-o", str(st_shader_path), str(scene_path)])
        assert st_shader_path.exists()

        st_shader = st_shader_path.read_text()
        assert st_shader == ref_st_shader
