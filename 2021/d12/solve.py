import fileinput
from collections import defaultdict


def build_graph(payload):
    graph = defaultdict(list)
    for line in payload:
        a, b = line.split("-")
        graph[a].append(b)
        graph[b].append(a)
    return graph


def dfs(node, graph, visited, dup, counter=0):
    if node == "end":
        return 1
    for adj in graph[node]:
        if adj.isupper():
            counter += dfs(adj, graph, visited, dup)
        else:
            if adj not in visited:
                counter += dfs(adj, graph, visited | {adj}, dup)
            elif dup and adj not in ("start", "end"):
                counter += dfs(adj, graph, visited, False)
    return counter


def part1(payload):
    graph = build_graph(payload)
    return dfs("start", graph, {"start"}, False)


def part2(payload):
    graph = build_graph(payload)
    return dfs("start", graph, {"start"}, True)


if __name__ == "__main__":
    payload = [line.strip() for line in fileinput.input()]
    print("part1", part1(payload))
    print("part2", part2(payload))
