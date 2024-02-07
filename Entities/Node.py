from dataclasses import dataclass


@dataclass
class Node:
    iposition: int
    jposition: int
    name: str = "."
