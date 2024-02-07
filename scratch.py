def update_graph(PG, init_infected, J, t):
    insert_infected(PG, init_infected)
    next_graph = PG
    for node in PG.nodes:
        neighbors = PG.nodes[node].neighbors
        k = PG.nodes[node].degree
        s = 0
        for i in neighbors:
            if i[state] == infected:
                s = s + 1
        u = infected_prob(s, k, t, J)
        r = rd.choice([0, 1], weights=[1 - u, u])  # Forse più semplice np.random.uniform(0,1)
        if r == 1:  # r<u
            next_graph.nodes[node][state] = infected
    PG = next_graph


def information_graphs(PG, VG, q=0.5):
    AP = nx.adjacency_matrix(PG)
    AG = nx.adjacency_matrix(VG)
    AI = np.matrix()
    for x, y in AP:
        r = np.random.uniform(0, 1)  # BINOMIAL
        if r < q:
            AI[x, y] = AG[x, y]
        else:
            AI[x, y] = AP[x, y]
    IG = nx.from_numpy_matrix(AI)
    return IG