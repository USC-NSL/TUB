# A Throughput-Centric View of the Performance of Datacenter Topologies


## Code Structure
- ```metric/``` code for computing throughput upper bound.
- ```topo_repo/``` contains a set of topologies (Jellyfish, Xpander, FatClique, Clos)
- ```utils/``` code for loading the topologies from file and generating maximal permutation traffic matrix.

## Dependencies
(1) Clone this repo<br>
```bash
$ git clone https://github.com/USC-NSL/TUB.git
```

(2) Python version<br>
This repo is tested with the following two combinations;
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


## Example

