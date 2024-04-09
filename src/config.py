import numpy as np
from src.utils import *

# Values for the tests
step = 0.1
js = np.arange(0, 200, step)  # Risk perception
ts = np.arange(0, 1+step, step)  # Tau values
qs = np.arange(0, 1+step, step)  # Connection probability for Information Graph

iterations = 10000  # Iteration
zero_threshold = 1e-4  # Zero threshold

# Values for the graph
n_nodes = 10  # Number of nodes
k = 6  # Number of edges to attach from a new node
prob_k = k / n_nodes  # Probability for random graph

# Values for the infection
init_infect = 5  # Initial infected nodes
perc_init_infect = 0.1  # Initial percentage of infected nodes


immunity = healthy  # Immunity
rec_prob = 0.1  # Recovery probability
