from .node import Node


class SimpleTree:
    root = Node

    def __init__(self, root_value: str, sub_nodes=[]):
        self.root.value = root_value
        self.root.sub_nodes = sub_nodes
