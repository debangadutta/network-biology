import networkx as nx

#Loading graph from path
graph_path = ".\directed_graph.graphml"
loaded_graph = nx.read_graphml(graph_path)
print(loaded_graph)

#Node and Edge attributes
node_attributes = loaded_graph.nodes.data()
edge_attributes = loaded_graph.edges.data()
print("Node attributes: ", node_attributes)
print("Edge attributes: ", edge_attributes)

#Centrality
degree_centrality = nx.degree_centrality(loaded_graph)
print("Degree Centrality: ", degree_centrality)

betweenness_centrality = nx.betweenness_centrality(loaded_graph)
print("Betweenness Centrality: ", betweenness_centrality)

closeness_centrality = nx.closeness_centrality(loaded_graph)
print("Closeness Centrality: ", closeness_centrality)

#Clustering Coefficients
average_clustering_coefficient = nx.average_clustering(loaded_graph)
print("Average Clustering Coefficient: ", average_clustering_coefficient)

node_clustering_coefficient = nx.clustering(loaded_graph, nodes="ALDOA")
print("Nodes Clustering: ", node_clustering_coefficient)

#Flows
maximum_flow_1 = nx.maximum_flow_value(loaded_graph, _s="HK1", _t="BPGM")
print("Maximum Flow (HK1->BPGM): ", maximum_flow_1)

maximum_flow_2 = nx.maximum_flow_value(loaded_graph, _s="Unknown", _t="BPGM")
print("Maximum Flow (Unknown->BPGM): ", maximum_flow_2)