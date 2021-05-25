from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import networkx as nx
import matplotlib.pyplot as plt

from utils import shortest_path
from utils import near_wc_tm
from metric import tub


class Topology(object):
    """General Topology Class

    Attributes:
        _topology: a networkx graph representing the switch connections
        _tor_list: a list of switch names with directly connected servers
        _demand_dict: a mapping from tor names to the number of their directly connected servers
    """

    def __init__(self, topology, tor_list, demand_dict):
        self._topology = topology
        self._tor_list = tor_list
        self._demand_dict = demand_dict

    def get_topology(self):
        return self._topology

    def get_tor_list(self):
        return self._tor_list

    def get_demand_dict(self):
        return self._demand_dict

    def draw_topology(self):
        nx.draw(self._topology)
        plt.show()

    def get_avg_path_between_src_dst(self, tor_list=None):
        return shortest_path.all_pair_shortest_path_length_adjacency_matrix(self.get_topology(), tor_list)

    def get_near_worst_case_traffic_matrix(self):
        return near_wc_tm.get_longest_matching_traffic_matrix(self.get_topology(),
                                                              self.get_tor_list(),
                                                              self.get_demand_dict())

    def get_tub(self):
        return tub.get_throughput_upper_bound(self.get_topology(), self.get_tor_list(), self.get_demand_dict())
