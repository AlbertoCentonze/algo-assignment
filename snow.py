import heapq


def main():
    VERTICES_NUMBER, EDGES_NUMBER, START, END = input_as_int_list()

    # print(f"v_n:{VERTICES_NUMBER} e_n:{EDGES_NUMBER} start:{START} end:{END}")
    raw_graph = []
    for i in range(EDGES_NUMBER):
        raw_graph.append(input_as_int_list())
    graph = Graph(raw_graph, VERTICES_NUMBER)
    graph.solve(START, END)


def input_as_int_list():
    return [int(x) for x in input().split()]


class Graph:
    def __init__(self, raw_graph: list[(int, int, int, int)], vertices: int):
        self.graph: dict[int, dict[int, (int, int)]] = {i + 1: {} for i in range(vertices)}
        for (start, end, length, snow) in raw_graph:
            self.graph[start][end] = (length, snow)
            self.graph[end][start] = (length, snow)

    def __repr__(self):
        output = ""
        for start, nested_dict in self.graph.items():
            output += f"from {start} \n"
            for end, (length, snow) in nested_dict.items():
                output += f"  -> {end}: length={length} snow={snow} \n"
        return output

    def calculate_distances(self, start, end):
        graph = self.graph

        # for each (thanks to dictionary comprehension)
        # dist[v] <- INFINITY
        dist = {vertex: float('infinity') for vertex in graph.keys()}
        # prev[v] <- UNDEFINED
        prev = {vertex: float('infinity') for vertex in graph.keys()}
        # add v to Q
        Q = [(0, start)]
        # dist[source] <- 0
        dist[start] = 0

        # while Q is not empty
        while len(Q) > 0:
            # u <- vertex in Q with min dist[u]
            dist_u, u = heapq.heappop(Q)

            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the priority queue.
            if dist_u > dist[u]:
                continue

            # here the edge length is in reality the snow, and the actual length is the length
            # for each neighbor v of u still in Q
            for v, (length, snow) in graph[u].items():
                alt = dist_u + length

                # Only consider this new path if it's better than any path we've
                # already found.
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(Q, (alt, v))

        return dist[end]

    def calculate_least_snow(self, start, end):
        graph = self.graph

        # for each (thanks to dictionary comprehension)
        # dist[v] <- INFINITY
        dist = {vertex: float('infinity') for vertex in graph.keys()}
        # prev[v] <- UNDEFINED
        prev = {vertex: float('infinity') for vertex in graph.keys()}
        # add v to Q
        Q = [(0, start)]
        # dist[source] <- 0
        dist[start] = 0

        while len(Q) > 0:
            # u <- vertex in Q with min dist[u]
            snow_u, u = heapq.heappop(Q)

            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the priority queue.
            if snow_u > dist[u]:
                continue
            # here the edge length is in reality the snow, and the actual length is the length
            # for each neighbor v of u still in Q
            for v, (length, snow) in graph[u].items():
                alt_snow = max(snow_u, snow)

                # Only consider this new path if it's better than any path we've
                # already found.
                if alt_snow < dist[v]:
                    dist[v] = alt_snow
                    prev[v] = u
                    heapq.heappush(Q, (alt_snow, v))

        return dist[end]

    def update_graph(self, snow_threshold):
        # set all paths with snow > snow_threshold to infinity
        for start, nested_dict in self.graph.items():
            for end, (length, snow) in nested_dict.items():
                if snow > snow_threshold:
                    self.graph[start][end] = (float('infinity'), snow)
                    self.graph[end][start] = (float('infinity'), snow)

    def solve(self, start, end):
        snow_threshold = self.calculate_least_snow(start, end)
        self.update_graph(snow_threshold)
        min_length = self.calculate_distances(start, end)
        if min_length == float('infinity') and snow_threshold == float('infinity'):
            print("Impossible")
        else:
            print(f"{snow_threshold} {min_length}")


if __name__ == '__main__':
    main()
