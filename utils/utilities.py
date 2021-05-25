from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import pickle


def get_model(filename):
    print("** Loading Model...")
    with open(filename, "rb") as file:
        if sys.version_info >= (3, 0):
            model = pickle.load(file, encoding="latin1")
        else:
            model = pickle.load(file)
    return model


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def store_model(model, file_path):
    print("** Storing Model...")
    delete_file(file_path)
    with open(file_path, "wb") as f:
        pickle.dump(model, f)
