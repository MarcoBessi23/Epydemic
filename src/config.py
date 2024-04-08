import numpy as np

from src.utils import *
# Values for the tests
step = 0.1
js = np.arange(0, 200, 0.1)  # Risk perception
ts = np.arange(0, 1+step, step)  # Tau values
qs = np.arange(0, 1+step, step)  # Connection probability for Information Graph

iterations = 1000  # Iteration
zero_threshold = 1e-6  # Zero threshold

# Values for the graph
n_nodes = 10  # Number of nodes
m = 6  # Number of edges to attach from a new node
prob_m = m / n_nodes  # Probability for random graph
init_infect = 1  # Initial infected nodes
percentage_init_infect = 0.5  # Initial percentage of infected nodes
immunity = healthy  # Immunity
rec_prob = 0.1  # Recovery probability
