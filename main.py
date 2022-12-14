import heapq


def main():
    VERTICES_NUMBER, EDGES_NUMBER, START, END = input_as_int_list()

    if EDGES_NUMBER <= 0:
        print("Impossible")
        return

    print(f"v_n:{VERTICES_NUMBER} e_n:{EDGES_NUMBER} start:{START} end:{END}")
    raw_graph = []
    for i in range(EDGES_NUMBER):
        raw_graph.append(input_as_int_list())
    graph = Graph(raw_graph, VERTICES_NUMBER)
    print(graph)
    print(graph.calculate_distances(START, END))


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

        snow_heights = {vertex: float('infinity') for vertex in graph.keys()}
        snow_heights[start] = 0
        pq = [(0, start)]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)

            # if current_vertex == end:
                # s = []  # emtpy sequence


            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the priority queue.
            if current_distance > snow_heights[current_vertex]:
                continue

            for neighbor, (length, snow) in graph[current_vertex].items():
                distance = current_distance + snow

                # Only consider this new path if it's better than any path we've
                # already found.
                if distance < snow_heights[neighbor]:
                    snow_heights[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return snow_heights


if __name__ == '__main__':
    main()
