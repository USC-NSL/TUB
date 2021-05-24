from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

from utils import utilities

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='compute throughput upper bound (TUB)')
    parser.add_argument('file_name', metavar='file_name', type=str, help='path to the topology file')
    args = parser.parse_args()
    print("=" * 10 + " Computing TUB " + "=" * 10)
    topology = utilities.get_model(args.file_name)
    tub = topology.get_tub()
    print("=" * 10 + " Result " + "=" * 10)
    print("TUB = ", tub)
