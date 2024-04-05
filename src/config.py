import numpy as np

from src.utils import healthy

# Values for the tests
js = np.arange(0.1, 200.1, 0.1)  # Risk perception
ts = np.arange(0.1, 1.1, 0.1)  # Tau values
qs = np.arange(0.1, 1.2, 0.2)  # Connection probability for Information Graph

iterations = 1000  # Iteration
zero_threshold = 1e-6  # Zero threshold

# Values for the graph
n_nodes = 10  # Number of nodes
m = 4  # Number of edges to attach from a new node
init_infect = 1  # Initial infected nodes
percentage_init_infect = 0.5  # Initial percentage of infected nodes
immunity = healthy  # Immunity
rec_prob = 0.1  # Recovery probability
