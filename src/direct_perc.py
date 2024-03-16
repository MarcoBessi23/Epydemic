import networkx as nx
import numpy as np
import random as rd

from matplotlib import pyplot as plt

from src.plot import plot_update
from src.utils import *


# funzione per aggiornare lo stato del nodo la uso ad ogni passaggio, deve restituire lo stato
def updating_node_percolation(G: nx.Graph, node: int, tau: float):
    res=False
    for node in G.neighbors[node]:
        r= np.random.uniform(0, 1)
        res= res or (tau>r and node[state]==infected)
    if res:
        return infected
    else:
        return  healthy

#Ho bisogno di copiare il grafo ad ogni passaggio e applicare la funzione di sopra ai nodi del grafi G, non finita
def simple_percolation(G: nx.graph, tau, iterations):
    
    for t in iterations:
        Support_graph = G.copy()
        for node in G.nodes:
            G.nodes[node][state] = updating_node_percolation(Support_graph,node,tau)


    return G


#taui[t+1]=min max(rij(t),taui(t)) calcolato per ogni vicino del nodo i
#Formula per aggiornare il valore tau[i] come indicato nella sezione simple percolation
#tau è un vettore tale che la componente i di tau corrisponde al valore di tau per il nodo i
#Partiamo dallo scenario in cui tutti i nodi sono infetti, quindi tau è un vettore di zeri. 
#Copio il vettore tau in un vettore ctau così da non sovrasvrivere il valore di tau ad ogni iterazione del min max
#La funzione nonzero ritorna indici corrispondenti ai vicini del nodo i, M è il vettore dei max da cui estraggo il
#minimo
def simple_tau_percolation(G: nx.graph, T: int):
    tau = np.zeros(nx.number_of_nodes(G))
    #Guardo le righe della matrice di adiacenza ad ogni iterazione per aggiornare il vettore 
    A = nx.adjacency_matrix(G) 
    for t in range(T):
        ctau = tau
        for i in range(len(tau)):
            M = []
            for j in range(np.nonzero(A[i])):
                r = np.random.uniform(0,1)
                M.append(np.max(r,ctau[j]))
            tau[i] = np.min(M)
    return tau



#INFECTION WITH RISK PERCEPTION

#Voglio ricavare parametro J per cui non c'è diffusione dell'infezione nel lungo periodo. 
# [J < −(k/s) ln(r/τ )] <--- condizione per cui un nodo si infetta, nella funzione estraggo r e controllo 
# se vale 1. J[i] è come sopra il valore minimo di J che fa infettare il nodo i. Salto i calcoli e vado
# direttamente alla formula (15) che è quella che vado ad implementare 
# Ji (t + 1) =max min (Jj(t), (ki/si[Jj(t)])*ln(rij(t)/τ))  si[J] è funzione che somma [Jj(t)>=J] per tutti i vicini

def critic_J_percolation(J, G: nx.graph, tau: float, T: int):
    A = nx.adjacency_matrix(G)
    for t in range(T):
        cJ = J
        for i in range(len(J)):
            m = []
            K = np.sum(A[i])
            for j in range(np.nonzero(A[i])):
                s = 0
                r = np.random.uniform(0,1)
                for k in range(np.nonzero(A[i])):
                    if cJ[k]>cJ[j]:
                        s = s+1
                m.append(np.min(cJ[j],(K/s)*np.log(r/tau)))
            J[i] = np.max(m)
    return J

                

                





