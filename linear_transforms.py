"""
Plot eigenvectors.

Figure 1: python linear_transforms.py "[[2, 0], [0, 1]]" "[[1, 0], [0, 1], [0.7, 0.7]]"
"""

from typing import List

import fire
from manim.mobject.geometry.line import Vector
from manim.scene.vector_space_scene import LinearTransformationScene


class EigenvectorDemonstration(LinearTransformationScene):
    """
    Basic visualization of the effect of a linear transform on a set of vectors.
    """

    def __init__(self, transform_matrix: List[List[float]], vectors: List[List[float]]) -> None:
        """
        Args:
            transform_matrix: nxn linear transform matrix.
            vectors: Vectors to visualize through the linear transform.
        """

        super().__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False
        )

        self.transform_matrix = transform_matrix
        self.vectors: List[Vector] = [Vector(vector) for vector in vectors]

    def construct(self):
        """
        Setup visualization.
        """

        for vector in self.vectors:
            self.add_vector(vector)

        self.apply_matrix(self.transform_matrix)
        self.wait(2)


def make_animation(transform_matrix: List[List[float]], vectors: List[List[float]]) -> None:
    """
    Create animation 3b1b-style animation of impact of linear transform on a set of vectors.

    Args:
        transform_matrix: nxn linear transform matrix.
        vectors: Vectors to visualize through the linear transform.
    """
    
    assert len(transform_matrix) == 2
    assert all(len(el) == 2 for el in transform_matrix)

    assert all(len(v) == 2 for v in vectors)

    scene = EigenvectorDemonstration(transform_matrix=transform_matrix, vectors=vectors)
    scene.render() 


if __name__ == "__main__":
    fire.Fire(make_animation)