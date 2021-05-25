from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gc
import igraph
import numpy as np

from networkx import nx
from utils import shortest_path


def get_longest_matching_traffic_matrix(topology, tor_list, demand_dict):
    """ Generates maximal permutation traffic matrix that results in near worst-case throughput

    This is a generalization to: Measuring and Understanding Throughput of Network Topologies
    (Sangeetha Abdu Jyothi, Ankit Singla, P. Brighten Godfrey, Alexandra Kolla), 2016

    Args:
        topology: a networkx graph representing switch connections
        tor_list: contains list of switches with directly connected servers
        demand_dict: a mapping from each ToR to its number of directly connected servers
    Returns:
        traffic_matrix: a dictionary (src, dst) --> amount of traffic
        sum_weight_matching: sum shortest_path_length(src, dst) * traffic_matrix(src, dst) over all pairs
                             traffic_matrix
    """

    # Line 30-36 makes sure the order of ToRs in the tor_list is the same as their order in the topology.nodes().
    initial_tor_list = list(tor_list)
    num_nodes = len(tor_list)
    tor_list = list()
    for node in topology.nodes():
        if node in initial_tor_list:
            tor_list.append(node)
    del initial_tor_list

    print("**** Computing all-pair shortest path lengths...")
    np_shortest_path = shortest_path.all_pair_shortest_path_length_adjacency_matrix(topology, tor_list)

    print("**** Generating bipartite graph...")
    bi_graph = igraph.Graph.Full_Bipartite(num_nodes, num_nodes)
    s = np.array(list(demand_dict.values()), order='F', dtype=np.uint16) * \
        (np.ones((num_nodes, num_nodes), order='F', dtype=np.uint16) - np.eye(num_nodes, order='F', dtype=np.uint16))
    minimum = np.min(np.array(list(demand_dict.values())))
    coefficient = np.minimum(s, np.transpose(s))/minimum
    weights = np.reshape(np.multiply(np_shortest_path, coefficient, dtype=np.float32, order='F'),
                         (1, num_nodes * num_nodes), order='F').tolist()[0]
    del s
    del coefficient
    del minimum
    gc.collect()

    print("**** Computing maximum weighted matching...")
    maximal_matching = bi_graph.maximum_bipartite_matching(weights=weights, eps=0.001)
    traffic_matrix = dict()

    sum_weight_matching = 0
    for i in range(num_nodes):

        j = maximal_matching.matching[i]
        if j >= num_nodes > i:
            j -= num_nodes
            s0 = tor_list[i]
            s1 = tor_list[j]
        elif i >= num_nodes > j:
            raise ValueError
        else:
            raise ValueError

        traffic_matrix[s0, s1] = min(demand_dict[s0], demand_dict[s1])
        sum_weight_matching += np_shortest_path[i][j] * traffic_matrix[s0, s1]

    return traffic_matrix, sum_weight_matching
