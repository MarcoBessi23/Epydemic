import networkx as nx

from src.infection import init_infected, get_information_graph, infection


def barabasi_albert_graph_test(nodes: int = 10, m: int = 2, q: float = 0.5, infected: int = 2):
    """
    Test the Barabasi Albert graph

    :param nodes:
    :param m:
    :param q:
    :param infected:
    :return:
    """
    PG = nx.barabasi_albert_graph(nodes, m)
    init_infected(PG, infected)
    VG = nx.barabasi_albert_graph(nodes, m)
    IG = get_information_graph(PG, VG, q)

    # plot_all_graphs(PG, VG, IG)
    infection(PG, 0.2, 0.1)


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


def scale_free_graph_test(nodes: int = 5, m: int = 5, q: float = 0.5, infected: int = 2):
    """
    Test the scale free graph

    :param nodes:
    :param m:
    :param q:
    :param infected:
    :return:
    """
    PG = nx.scale_free_graph(nodes)
    PG = nx.to_undirected(PG)  # TODO: Check if it is necessary
    init_infected(PG, infected)
    VG = nx.scale_free_graph(nodes)
    IG = get_information_graph(PG, VG, q)

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

    # plot_all_graphs(PG, VG, IG)
    infection(PG, 0.2, 0.1)


def main():
    # cycle_graph_test()
    scale_free_graph_test()
    # random_graph_test() TODO: Check components graphs divided by zero


if __name__ == "__main__":
    main()
