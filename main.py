import networkx as nx
import xml.etree.ElementTree as ET

pathFile = ""
try:
    pathFile = nx.read_graphml("problem.graphml")
except ET.ParseError as e:
    print("Error parsing GraphML file:", e)


def rateCardA(length=1):
    rateCardDict = {
        "Cabinet": 1000,
        "verge": 50 * length,
        "road": 100 * length,
        "Chamber": 200,
        "Pot": 100,
    }
    return rateCardDict


def rateCardB(length=1, lengthOfTrench=1):
    rateCardDict = {
        "Cabinet": 1200,
        "verge": 40 * length,
        "road": 80 * length,
        "Chamber": 200,
        "Pot": 20 * lengthOfTrench,
    }
    return rateCardDict


def calculateTrenchLength(tree, source, target):
    length = 0
    path = nx.shortest_path(tree, source, target)
    for i in range(len(path) - 1):
        sourceEdge = path[i]
        destinationEdge = path[i + 1]
        edge_length = tree.get_edge_data(sourceEdge, destinationEdge)["length"]
        length += edge_length
    return length


def calculateRateCardA():
    totalRateCardOfA = 0
    for node in pathFile.nodes(data=True):
        value = rateCardA()[node[1]["type"]]
        totalRateCardOfA += value

    for edge in pathFile.edges(data=True):
        value = rateCardA(edge[2]["length"])[edge[2]["material"]]
        totalRateCardOfA += value

    return totalRateCardOfA


def calculateRateCardB():
    totalRateCardOfB = 0
    for node in pathFile.nodes(data=True):
        root = [x for x, y in pathFile.nodes(data=True)
                if y['type'] == "Cabinet"]
        trenchLength = calculateTrenchLength(pathFile, root[0], node[0])
        value = rateCardB(1, trenchLength)[node[1]["type"]]
        totalRateCardOfB += value

    for edge in pathFile.edges(data=True):
        value = rateCardB(edge[2]["length"])[edge[2]["material"]]
        totalRateCardOfB += value

    return totalRateCardOfB


print("Total of Rate Card A : ", calculateRateCardA())
print("Total of Rate Card B : ", calculateRateCardB())
