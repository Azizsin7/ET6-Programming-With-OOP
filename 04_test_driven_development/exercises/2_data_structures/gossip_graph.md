# GossipGraph

Write a class called `GossipGraph`. People spread gossip to their friends. Each person is a node.

## Instance Data

- One option is to structure your data as a dict of lists with each name being a key, and the lists storing other names/keys.

## Required behaviors

- `add_person(name)`
- `connect(name1, name2)` — people become friends (bidirectional)
- `spread_gossip(source)` — returns list of people who will hear the gossip, in order (you can use BFS)

## Later spec

- Add `block(name1, name2)` — stops gossip from spreading between those two friends.
- Add `gossip_path(source, target)` — return the path gossip takes from one person to another (or `None` if blocked)
