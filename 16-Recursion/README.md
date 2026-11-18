# How did I solve recursion problems in python?
# Python Bootstrap Recursion

A quick reference for deep recursive problems (for example, DFS on a long chain) when normal Python recursion may exceed the interpreter's recursion-depth limit.

> **Idea:** Keep suspended generator calls in a Python list and manage them with a loop. Bootstrap avoids deeply nested Python calls, but still uses O(depth) memory.

## 1. Bootstrap template

```python
from types import GeneratorType


def bootstrap(f, stack=None):
    if stack is None:
        stack = []

    def wrapper(*args, **kwargs):
        if stack:                         # Recursive call: only create a generator.
            return f(*args, **kwargs)

        to = f(*args, **kwargs)            # First call: start the manager.
        while True:
            if isinstance(to, GeneratorType):
                stack.append(to)           # Push suspended call.
                to = next(to)              # Run it until its next yield.
            else:
                stack.pop()                # Current call has produced its result.
                if not stack:
                    break                  # Original call is finished.
                to = stack[-1].send(to)    # Give result to the waiting parent.

        return to

    return wrapper
```

## 2. Convert normal recursion

Normal version:

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
```

Bootstrap version:

```python
@bootstrap
def fact(n):
    if n == 0:
        yield 1
        return

    small = yield fact(n - 1)
    yield n * small
```

**Conversion pattern:**

- `return base` → `yield base` followed by `return`.
- `small = f(smaller)` → `small = yield f(smaller)`.
- `return answer` → `yield answer`.

Each invocation must yield **one final ordinary result**. Do not put more work after that final `yield`.

## 3. How bootstrap works internally

1. The first call enters `wrapper` with an empty `stack`. It creates the first generator and starts the manager loop.
2. A recursive call enters `wrapper` while `stack` is non-empty. It returns a generator object; it does not start another manager.
3. The parent reaches `yield child_call`. The manager recognises the child generator, pushes it onto `stack`, and starts it with `next()`.
4. The child eventually yields an ordinary value (its result). The manager pops the child and sends that value to the waiting parent using `.send(result)`.
5. The parent's `yield` expression receives the result. The parent continues, calculates its answer, and yields its own final result.
6. This repeats until the original generator is popped and `stack` becomes empty. The wrapper returns the final result.

| Operation | Meaning |
|---|---|
| `stack.append(gen)` | Push a suspended call onto the explicit stack. |
| `next(gen)` | Start/resume a generator until it yields. |
| `parent.send(result)` | Resume the parent and pass it the child's result. |

**Mental model:** `yield child()` pauses the parent and asks the manager to run the child. `.send(result)` resumes the parent as though the child call has returned that result.

## 4. Example: print all matching positions

Prints **1-based positions in increasing order**. The recursive call happens first, so printing occurs while calls unwind.

```python
@bootstrap
def print_occurrences(a, n, x):
    if n == 0:
        yield None
        return

    yield print_occurrences(a, n - 1, x)

    if a[n - 1] == x:
        print(n, end=" ")

    yield None
```

## 5. Remember

- Use bootstrap for genuinely deep recursion; normal recursion is simpler for shallow problems.
- The explicit list and generator frames still require **O(depth)** auxiliary memory.
- Recursive calls must be written as `yield f(...)`.
- This simple wrapper expects generator functions and the yield-as-result convention. A normal `return value` inside the generator is not handled by it.
- This version is intended for self-recursive functions. Mutual recursion and exception-safe stack cleanup need a more advanced manager.
- An iterative DFS/stack is another option and may be more efficient.
