from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from utils import near_wc_tm


def get_throughput_upper_bound(topo, tor_list, demand_dict):
    """ Computes the throughput upper bound (tub)

    Args:
        topo: a networkx graph representing switch connections
        tor_list: contains list of switches with directly connected servers
        demand_dict: a mapping from each ToR to its number of directly connected servers

    Returns:
        tub: throughput upper bound
    """
    print("** Computing maximal permutation traffic matrix...")
    _, sum_weight_matching = near_wc_tm.get_longest_matching_traffic_matrix(topo, tor_list, demand_dict)
    print("** Computing TUB...")
    tub = len(topo.edges()) * 2.0 / sum_weight_matching
    return tub
