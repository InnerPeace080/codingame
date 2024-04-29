import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

graph: dict[int, list[int]] = {}
gateways: list[int] = []

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    graph.setdefault(n1, []).append(n2)
    graph.setdefault(n2, []).append(n1)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)

# print graph
for node in graph:
    print(f"{node}: {graph[node]}", file=sys.stderr, flush=True)

node_queue: list[int] = []
node_queue_path: list[list[int]] = []
processed_nodes: list[int] = []


def shortest_to_gateway(node_id, prev_path: list[int] = []) -> list[int]:
    processed_nodes.append(node_id)

    if not prev_path:
        prev_path = [node_id]

    print(f"prev_path = {prev_path}", file=sys.stderr, flush=True)
    # if node_id is a gateway, return 0
    if node_id in gateways:
        return prev_path

    print(f"graph[node_id] = {graph[node_id]}", file=sys.stderr, flush=True)
    for next_node in graph[node_id]:
        # if next_node is not in node_queue, add it
        if next_node not in processed_nodes and next_node not in node_queue:
            node_queue.append(next_node)
            node_queue_path.append(prev_path)

    while node_queue:
        print(f"Node queue: {node_queue}", file=sys.stderr, flush=True)
        next_node = node_queue.pop(0)
        next_node_prev_path = node_queue_path.pop(0)

        return shortest_to_gateway(next_node, next_node_prev_path + [next_node])

    return []  # Add this line to return an empty list if no gateway is found

    # game loop
while True:
    # reset global variables
    node_queue = []
    node_queue_path = []
    processed_nodes = []

    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    path_to_gateway = shortest_to_gateway(si)

    print(f"Path to gateway: {path_to_gateway}", file=sys.stderr, flush=True)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(f"{path_to_gateway[-2]} {path_to_gateway[-1]}")
    # update graph
    graph[path_to_gateway[-2]].remove(path_to_gateway[-1])
    graph[path_to_gateway[-1]].remove(path_to_gateway[-2])
