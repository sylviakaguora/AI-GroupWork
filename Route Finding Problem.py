import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_edge("SportsComplex", "Siwaka")

g.add_edge("Siwaka", "Ph1.A")
g.add_edge("Siwaka", "Ph1.B")

g.add_edge("Ph1.A", "Ph1.B")
g.add_edge("Ph1.A", "Mada")

g.add_edge("Ph1.B", "Phase2")
g.add_edge("Ph1.B", "STC")

g.add_edge("Phase2", "J1")
g.add_edge("Phase2", "STC")
g.add_edge("Phase2", "Phase3")

g.add_edge("J1", "Mada")

g.add_edge("STC", "ParkingLot")

g.add_edge("Phase3", "ParkingLot")

g.add_edge("Mada", "ParkingLot")

nx.draw(g, with_labels=True)
plt.savefig("graph1.png")

