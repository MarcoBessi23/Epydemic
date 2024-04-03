import numpy as np

from src.utils import healthy

# Values for the tests
js = np.arange(0.05, 20.05, 0.05)  # Risk perception
ts = np.arange(0.05, 1.05, 0.05)  # Tau values
iterations = 1000  # Iteration
zero_threshold = 1e-6  # Zero threshold

# Values for the graph
n_nodes = 20  # Number of nodes
m = 4  # Number of edges to attach from a new node
init_infect = 1  # Initial infected nodes
percentage_init_infect = 0.5  # Initial percentage of infected nodes
immunity = healthy  # Immunity
rec_prob = 0.1  # Recovery probability
