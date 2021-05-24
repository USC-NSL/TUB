from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import networkx as nx
import scipy

from typing import List


def sum_all_pair_shortest_path_length_adjacency_matrix(g: nx.Graph) -> int:
    """ Computes the sum of shortest path length over all the pairs of nodes in g

    Args:
        g: a networkx graph representing the connection between switches.

    Returns:
        total_sp: sum of shortest path length over all the pairs of nodes in g
    """

    num_node = len(g.nodes())
    A = nx.to_numpy_matrix(g, order='F', dtype=np.float32)
    B = np.eye(num_node, order='F', dtype=np.float32)
    total_sp = num_node * (num_node - 1) - num_node
    C = np.zeros(np.shape(A), order='F', dtype=np.float32)
    for k in range(num_node - 1):
        B = scipy.linalg.blas.sgemm(1, B, A)
        # B = np.matmul(B, A)
        C = np.add(C, B)
        num = np.count_nonzero(C == 0)
        if num == 0:
            break
        total_sp += num

    return total_sp


def all_pair_shortest_path_length_adjacency_matrix(g: nx.Graph, tor_list: List = None) -> np.array:
    """ Returns the length of the shortest path between all pairs of ToRs

        Args:
            g: a networkx graph representing the connection between switches.
            tor_list: a list of tors such that the output represents the shortest path length among pairs
                with both ends in tor_list. In case tor_list = None, this function returns the shortest
                path length between all the pairs.
        Returns:
            shortest_path_np_array:
        """

    num_node = len(g.nodes())
    A = nx.to_numpy_matrix(g, order='F', dtype=np.float32)
    B = np.eye(num_node, order='F', dtype=np.float32)

    C = np.eye(num_node, order='F', dtype=np.float32)
    shortest_path_np_array = np.ones(np.shape(A), order='F', dtype=np.float32)

    for k in range(num_node - 1):
        B = scipy.linalg.blas.sgemm(1, B, A)
        C = np.add(C, B)
        if np.count_nonzero(C == 0) == 0:
            break

        add_np_array = np.subtract(np.ones(np.shape(C), order='F', dtype=np.float32), C)
        add_np_array = np.where(add_np_array < 0, 0, add_np_array)
        shortest_path_np_array = np.add(shortest_path_np_array, add_np_array)
        del add_np_array

    shortest_path_np_array = np.subtract(shortest_path_np_array, np.eye(num_node, order='F', dtype=np.float32))
    delete_index_list = list()
    if tor_list:
        for index, node in enumerate(g.nodes()):
            if node not in tor_list:
                delete_index_list.append(index)
        shortest_path_np_array = np.delete(shortest_path_np_array, delete_index_list, axis=1)
        shortest_path_np_array = np.delete(shortest_path_np_array, delete_index_list, axis=0)

    del A
    del B
    del C
    return shortest_path_np_array
