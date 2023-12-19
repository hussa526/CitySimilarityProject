"""
this file creates a graph using functions from personalprject.py and calculates the max node centrality
"""
import personalprject
import networkx as nx
import matplotlib.pyplot


def create_graph_and_nodes(newdict: dict) -> nx.Graph():
    """
    this function takes in a dictionary, and creates a graph and nodes according to the key values (doesn't look at any
    associated values)
    """
    graph = nx.Graph()
    for item in newdict:
        graph.add_node(item)
    return graph


def add_edges(graph: nx.Graph(), neighbouring_dict: dict) -> nx.Graph():
    """
    takes in graph from create_graph_and_nodes and adds edges between the nodes using personalprject.dict_of_
    neighbours()
    """
    for city1 in neighbouring_dict:
        for city2 in neighbouring_dict[city1]:
            graph.add_edge(city1, city2, weight=0.07)
    return graph


def display_graph(graph: nx.Graph()) -> None:
    """
    displays the graph produced from add_edges()
    """
    pos = nx.spring_layout(graph, k=0.25, seed=40)
    nx.draw(graph, pos, with_labels=True, node_size=150, edge_color='red', width=2.0, font_weight='bold', font_size=9.0)
    matplotlib.pyplot.show()


def max_node_centrality(graph: nx.Graph()) -> str:
    """
    creates a dictionary mapping cities to the number of edges they have, and returns the city with the most edges
    """
    centrality = nx.degree_centrality(graph)
    max_degree_centrality_node = max(centrality, key=centrality.get)
    return max_degree_centrality_node


if __name__ == '__main__':
    import python_ta

    #python_ta.check_all(config={
     #'extra-imports': [],  # the names (strs) of imported modules
     #'allowed-io': [],  # the names (strs) of functions that call print/open/input
     #'max-line-length': 120
     #})
