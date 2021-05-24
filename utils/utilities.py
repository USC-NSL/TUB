from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import pickle

from topo_repo import topology


def get_model(filename: str) -> topology.Topology:
    print("** Loading Topology...")
    with open(filename, "rb") as file:
        model = pickle.load(file, encoding="latin1")
    return model


def delete_file(file_path: str) -> None:
    if os.path.exists(file_path):
        os.remove(file_path)


def store_model(model, file_path: str) -> None:
    delete_file(file_path)
    with open(file_path, "wb") as f:
        pickle.dump(model, f)
