import networkx as nx
import numpy as np
from src.infection import init_infected, get_information_graph, infection
from src.plot import plot_all_graphs, plot_graph



def cycle_graph_test(nodes: int = 20, m: int = 2, q: float = 0.5, infected: int = 3):
    """
    Test the cycle graph

    :param nodes:
    :param m:
    :param q:
    :param infected:
    :return:
    """
    PG = nx.cycle_graph(nodes)
    init_infected(PG, infected)
    VG = nx.cycle_graph(nodes)
    IG = get_information_graph(PG, VG, q)

    # plot_all_graphs(PG, VG, IG)
    infection(PG, 0.2, 0.1, 0.3, immunity= False)


#Aggiunto scale free come nel paper? Non so cosa non funziona
def scale_free_graph_test(nodes: int = 5, m: int = 3, q: float = 0.5, infected: int = 2):
    """
    Test the scale free graph
    
    :param nodes:
    :param m:
    :param q:
    :param rec_prob:
    :param infected:
    :return:
    """
    PG = nx.barabasi_albert_graph(nodes, m)
    init_infected(PG, infected)
    VG = nx.barabasi_albert_graph(nodes,m)
    IG = get_information_graph(PG, VG, q)
    plot_all_graphs(PG, 0.2, 0.1)
    infection(PG, 0.2, 0.1, 0.3, immunity = False)

def random_graph_test(nodes: int = 10, p: int = 0.4, q: float = 0.5, infected: int = 2):
    """
    Test the random graph

    :param nodes:
    :param p:
    :param q:
    :param infected:
    :return:
    """
    PG = nx.gnp_random_graph(nodes, p)
    init_infected(PG, infected)
    VG = nx.gnp_random_graph(nodes, p)
    IG = get_information_graph(PG, VG, q)

    #plot_all_graphs(PG, VG, IG)
    infection(PG, 0.2, 0.1)


risk_perceptions= np.arange(0,50)
taus = np.arange(0, 1, 0.1)

def get_J_critical(G: nx.graph,rec_prob= 0.2):
    values = []
    for t in taus:
        j= 0
        while(infection(G, j, t, rec_prob, immunity= False)>0 and j<len(risk_perceptions) ):
            v = infection(G, j, t, rec_prob, immunity= False)
            j= j+1
        if v == 0:
            values.append((t,j))
    return values

        
            

    


def main():
    taus = np.arange(0, 1, 0.1)
    #cycle_graph_test()
    scale_free_graph_test()
    # random_graph_test() TODO: Check components graphs divided by zero


if __name__ == "__main__":
    main()
