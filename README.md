# A Throughput-Centric View of the Performance of Datacenter Topologies
This repository contains the code for computing throughput upper bound (TUB). TUB is tight and scalable metric for 
estimating worst-case throughput of uni-regular and bi-regular topologies, 
and very useful to testing whether a designed topology is non-blocking or not (ie, can support every traffic 
matrix without the need to drop any traffic).

# Instructions
## Code Structure
- ```metric/``` code for computing throughput upper bound.
- ```topo_repo/``` contains a set of topologies (Jellyfish, Xpander, FatClique, Clos)
- ```utils/``` code for loading/storing the topologies and generating maximal permutation traffic matrix.

## Installation
(1) Clone this repo<br>
```bash
$ git clone https://github.com/USC-NSL/TUB.git
```

(2) Python version. This repo is tested with the following two combinations;
- Python 2.7.17 + pip 20.2.3 (used to generate results of the paper)
- Python 3.7.10 + pip 21.1.1

(3) Install dependencies<br>
``` bash
$ pip install -r requirements.txt
```

Required dependencies:<br>
- networkx
- scipy
- numpy
- python-igraph
- matplotlib


## How to use?
There are two ways of using this repository; <br>
(1) **Storing the topology and computing the TUB using ```main_tub.py```.**
``` bash
$ python main_tub.py path_to_topology_file
```
In order to use this approach, you should store your topology in the format of ```Topology``` class
provided under ```topo_repo/topology.py```. After you initialized the class, you can call 
```store_model(model, file_path)``` from ```utils/utilities.py``` to store the topology.

*Examples*. For each topology family used in the paper (Jellyfish, Xpander, FatClique, Clos), we have provided a
few examples in ```topo_repo/``` using which you can try TUB. For example, to compute TUB on Jellyfish with 32K servers and 8 
servers per switch, you can try the following.
``` bash
$ python main_tub.py topo_repo/Jellyfish/jf_R_32_H_8_N_32000 
``` 

(2) **Direct function call.** <br>
Alternatively, you can call ```get_throughput_upper_bound()``` from ```metric/tub.py``` in your code.
The function gets three inputs and computes the TUB. 
Please visit ```metric/tub.py``` for more information.

**Note**. Depending on your computing resources, you might face out-of-memory error when trying to
compute the TUB on some of the provided examples.
* Using a 64GB machine, we are able to compute TUB for all the examples
* Using a 32GB machine, we can compute TUB for all except Jellyfish and Xpander with ~128K servers.


