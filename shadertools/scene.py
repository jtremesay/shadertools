from dataclasses import dataclass, field


@dataclass
class Vector3:
    x: float
    y: float
    z: float


@dataclass
class Node:
    pass


@dataclass
class Camera:
    position: Vector3 = field(default_factory=lambda: Vector3(0, 0, 0))
    view_port: Vector3 = field(default_factory=lambda: Vector3(1, 1, 1))


@dataclass
class Scene:
    root: Node
    camera: Camera = field(default_factory=Camera)


@dataclass
class Material:
    color: Vector3
    specular: float = 0.0


@dataclass
class Sphere(Node):
    center: Vector3
    radius: float
    material: Material


@dataclass
class SdfUnion(Node):
    nodes: list[Node] = field(default_factory=list)
