# UndoList

Write a class called `UndoList`. It's like a list that remembers its edits.

## Instance Data

- root node
- edits: list

## Required behaviors

- `add(item)`
- `remove(item)`
- `get_items()` returns all current items
- `undo()` — undoes the most recent change (`add` or `remove`)

## Later spec

- Add `redo()` to reapply the most recently undone action.
- Add `history()` to return a list of past actions (`"add A"`, `"remove B"`, etc.)
