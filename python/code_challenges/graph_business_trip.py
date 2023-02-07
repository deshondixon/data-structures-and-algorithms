from data_structures.graph import Graph


def direct_flights(graph, itinerary):
    cost = 0
    for i in range(len(itinerary) - 1):
        city1 = itinerary[i]
        city2 = itinerary[i + 1]
        flight = graph.get_flight(city1, city2)
        if flight:
            cost += flight.cost
        else:
            return False, cost
    return True, cost

