import networkx as nx

from src.infection import init_infected, get_information_graph, infection
from src.plot import plot_all_graphs, plot_graph



def cycle_graph_test(nodes: int = 20, m: int = 2, q: float = 0.5, infected: int = 2):
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
    infection(PG, 0.2, 0.1)


#Aggiunto scale free come nel paper? Non so cosa non funziona
def scale_free_graph_test(nodes: int = 5, m: int = 5, q: float = 0.5, infected: int = 2):
    """
    Test the scale free graph

    :param nodes:
    :param m:
    :param q:
    :param infected:
    :return:
    """
    PG = nx.powerlaw_cluster_graph(nodes, m, 0)
    init_infected(PG, infected)
    VG = nx.powerlaw_cluster_graph(nodes, m, 0)
    IG = get_information_graph(PG, VG, q)
    plot_all_graphs(PG, 0.2, 0.1)
    infection(PG, 0.2, 0.1)

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


    
def graph_boh_test():    
    n, t = 10, 2
    while True:  # Continue generating sequences until one of them is graphical, quando è graphical vuol dire che esiste un grafo che ha quella distribuzione
        seq = sorted([int(round(d)) for d in nx.powerlaw_sequence(n, t)], reverse=True)  # Non funziona powerlaw sequence, prova sul tuo
        if nx.is_graphical(seq):
            break
    PG = nx.random_degree_sequence_graph(seq, tries=100)  # Adjust number of tries as you see fit
    #plot_graph(PG)


def main():
    # cycle_graph_test()
     scale_free_graph_test()
    # graph_boh_test()
    # random_graph_test() TODO: Check components graphs divided by zero


if __name__ == "__main__":
    main()
