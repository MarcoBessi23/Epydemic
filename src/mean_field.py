import scipy

from src.infection import infected_prob


def simulated_mean_field_infection(k: int, tau: float, c: float, T: int, J: float) -> float:
    """
    Simulated mean field infection
    Function to simulate the evolution of an infection through mean field approximation

    :param k: degree of the graph
    :param tau: bare infection probability
    :param c: initial percentage of infected nodes
    :param T: iteration
    :param J: perception risk
    :return: return of the percentage of infected nodes
    """
    # FIXME: nan values from the scipy.special.binom and pow functions?
    for _ in range(T):
        # binoms = [scipy.special.binom(k, s) for s in range(1, k + 1)]
        # infected_probs = [infected_prob(s, k, tau, J) for s in range(1, k + 1)]
        # pows = [pow(c, s) * pow(1 - c, k - s) for s in range(1, k + 1)]
        c = sum(scipy.special.binom(k, s) * pow(c, s) * pow(1 - c, k - s) * s * infected_prob(s, k, tau, J)
                for s in range(1, k + 1))
    return c
