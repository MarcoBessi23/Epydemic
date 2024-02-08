import networkx as nx

from src.infection import init_infected, get_information_graph, infection


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


def scale_free_graph_test(nodes: int = 20, m: int = 5, q: float = 0.5, infected: int = 2):
    """
    Test the scale free graph

    :param nodes:
    :param m:
    :param q:
    :param infected:
    :return:
    """
    PG = nx.scale_free_graph(nodes)
    init_infected(PG, infected)
    VG = nx.scale_free_graph(nodes)
    IG = get_information_graph(PG, VG, q)

    infection(PG, 0.2, 0.1)


def main():
    cycle_graph_test()
    # scale_free_graph_test()


if __name__ == "__main__":
    main()
