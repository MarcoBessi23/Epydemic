import networkx as nx
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from src.config import ts, qs
from src.utils import *


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
        nx.draw(G, pos, ax=ax, node_color=blue, with_labels=True,
                arrows=True, arrowstyle='->', arrowsize=10)
    else:
        nx.draw(G, pos, ax=ax, node_color=blue, with_labels=True,)
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


def plot_update(G: nx.Graph, pos: dict) -> None:
    """
    Plot the updated graph G

    :param G: graph
    :param pos: position of the nodes
    """
    colors = [blue if G.nodes[node][state] == healthy else green if G.nodes[node][state] == recovered else red for node in G]
    nx.draw(G, node_color=colors, with_labels=True, pos=pos)
    plt.pause(1)


def plot_critical_j(critics: dict, file: str, prediction: bool = True) -> None:
    """
    Plot the critical J values

    :param critics: dict of critical values
    :param file: file name
    :param prediction: if the prediction should be plotted
    """
    plt.title("Critical J values")
    plt.plot(critics[t_test], critics[j_test], label="Critical J", color=blue, marker="o", linestyle="-")
    if prediction:
        plt.plot(critics[t_test], critics[j_pred], label="Predicted J", color=black, marker="", linestyle="--")
    plt.xlabel("Tau")
    plt.ylabel("Jc")
    plt.legend()
    plt.savefig(path_plots + file)
    plt.show()


def plot_critical_t(critics: dict, file: str, prediction: bool = True) -> None:
    """
    Plot the critical tau values

    :param critics: dict of critical values
    :param file: file name
    :param prediction: if the prediction should be plotted
    """
    plt.title("Critical Tau values")
    plt.plot(critics[t_test], critics[t_test], label="Critical Tau", color=blue, marker="o", linestyle="-")
    if prediction:
        plt.plot(critics[t_test], critics[t_pred], label="Predicted Tau", color=black, marker="", linestyle="--")
    plt.xlabel("Tc")
    plt.ylabel("Tc")
    plt.legend()
    plt.savefig(path_plots + file)
    plt.show()


def plot_q_value(critics: dict, file: str, prediction: bool = True) -> None:
    """
    Plot the value of the Information Graph
    :param critics:
    :param file:
    :param prediction:
    :return:
    """
    plt.title("Phase diagram")
    fig = plt.figure()

    # Aggiunta di un asse 3D
    ax = fig.add_subplot(111, projection='3d')

    # Creazione del grafico 3D
    ax.scatter(critics[t_test], critics[q_test], critics[j_pred], c='r', marker='o')

    # Impostazione dei titoli degli assi
    ax.set_xlabel('Tau')
    ax.set_ylabel('Q')
    ax.set_zlabel('Jc')

    plt.show()
    