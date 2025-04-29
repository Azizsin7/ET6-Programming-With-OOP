# Graph + Node
s
Create two classes: `GraphNode` and `Graph`.

## Required behaviors

- `add_node(label)`
- `connect(a, b)` — connect two node labels (bidirectional)
- `get_neighbors(label)` — return list of connected labels
- `has_path(a, b)` — return `True` if any path exists, you do not need to return the path

## Later spec

- Add `disconnect(a, b)` to remove an edge if it exists.
- Add `shortest_path(a, b)` that returns the shortest path as a list of labels (you can use BFS).
