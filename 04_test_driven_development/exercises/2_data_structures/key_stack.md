# KeyStack

Write a class called `KeyStack`. It’s like a stack, but it can be locked.

## Required behaviors

- `push(item)`
- `pop()`
- `lock(key)`
- `unlock(key)` - only unlocks the stack if the _key_ argument matches the key used to lock the stack.
- `is_locked()` returns whether the stack is locked
  > When locked, `push` and `pop` do nothing.

## Later spec

- Add `change_key(old_key, new_key)`
- Add `get_snapshot()` that returns a list of items (only works if unlocked)
