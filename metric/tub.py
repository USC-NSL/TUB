from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from utils import near_wc_tm


def get_throughput_upper_bound(topo, tor_list, demand_dict):
    print("** Computing maximal permutation traffic matrix...")
    _, sum_weight_matching = near_wc_tm.get_longest_matching_traffic_matrix(topo, tor_list, demand_dict)
    print("** Computing TUB...")
    tub = len(topo.edges()) * 2.0 / sum_weight_matching
    return tub
