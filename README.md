# Distance Vector Routing

Distance Vector Routing (DVR) protocols use a fully distributed algorithm that finds the shortest path by solving the <a href="https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm">Bellman-Ford algorithm</a> at each node. Here, we implement a distributed version of the Bellman-Ford algorithm and use it to calculate routing paths in a network.

In "pure" DVR protocols, the hop count determines the distance between nodes. But, some DVR protocols that operate at higher levels (like the border gateway protocol) make routing decisions based on business relationships (or weightings) in addition to a hop count. Our implementation considers weighted (including negative weights), directed links in our network topologies (represented in `Topology.py`).

In this simulation, we can think of nodes (i.e., router; represented in `Node.py`) as individual autonomous systems (ASes) and the weights on the links as a reflection of the business relationship between ASes.

`DistanceVector.py` is a specialization of the `Node` class that represents a network node running the DVR algorithm.

To simulate a specific topology, execute the `run.sh` bash script: `./run.sh *Topo`

This will execute the DVR algorithm on the topology defined in `*Topo.txt` and log the results to `*Topo.log`. For example: `./run.sh topo1` will execute the DVR algorithm on the topology defined in `topo1.txt` and log the results to `topo1.log`. See the `DVR_tests` folder for examples of correctly formatted topology files and an incorrectly formatted topology file (`BadTopo.txt`).
