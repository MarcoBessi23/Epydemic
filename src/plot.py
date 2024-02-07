import networkx as nx
from matplotlib import pyplot as plt


def plot_graph(G: nx.Graph, pos: dict, ax, oriented: bool = False, show: bool = False) -> None:
    """
    Plot the graph G

    :param G: graph
    :param ax: axis
    :param pos: position of the nodes
    :param oriented: if the graph is oriented
    :param show: if the graph should be displayed
    """
    if oriented:
        nx.draw(G, pos, ax=ax, node_color='cornflowerblue', with_labels=True,
                arrows=True, arrowstyle='->', arrowsize=10)
    else:
        nx.draw(G, pos, ax=ax, node_color='cornflowerblue', with_labels=True,)
    if show:
        plt.show()


def plot_all_graphs(PG: nx.Graph, VG: nx.Graph, IG: nx.Graph) -> None:
    """
    Plot the graphs PG, VG and IG

    :param PG: physical graph
    :param VG: virtual graph
    :param IG: information graph
    """
    fig, axs = plt.subplots(1, 3)
    axs[0].set_title("Physical Graph")
    axs[1].set_title("Virtual Graph")
    axs[2].set_title("Information Graph")

    pos = nx.spring_layout(PG)

    plot_graph(PG, pos, ax=axs[0])
    plot_graph(VG, pos, ax=axs[1])
    plot_graph(IG, pos, ax=axs[2], oriented=True)

    plt.show()


def plot_update(G: nx.Graph, pos: dict, ax, show: bool = False) -> None:
    """
    Plot the updated graph G

    :param G: graph
    :param pos: position of the nodes
    :param ax: axis
    :param show: if the graph should be displayed
    """
    nx.draw(G, pos, ax=ax, node_color='cornflowerblue', with_labels=True)
    if show:
        plt.show()