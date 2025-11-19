from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_scene(path: Path):
    """Load a scene from a Python file."""
    scene_module_name = path.stem
    spec = spec_from_file_location(scene_module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {path}")
    scene_module = module_from_spec(spec)
    spec.loader.exec_module(scene_module)

    # Create the scene and compile the shader
    return scene_module.create_scene()
