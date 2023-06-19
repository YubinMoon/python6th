import collections

graph = {
    "A": ["B", "C"],
    "B": ["A", "B", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

visited = set()


def bfs_iterative(start_node):
    queue = collections.deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
    visited.clear()
    print()


def dfs_iterative(start_noe):
    stack = [start_noe]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))
    visited.clear()
    print()


snode = "A"
dfs_iterative(snode)
bfs_iterative(snode)
