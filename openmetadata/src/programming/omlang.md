### Omlang, pure programmable content

In traditional programming, variable definitions and their values are stored together with their business logic. Conversely, Omlang separates storage from usage.

```python
# Variables and values are stored on disk
content
|-- red
|-- green
|-- blue
```

```python
# The variables are then used in Omlang as follows:
 color = red + green + blue
```

# Architecture

Omlang is designed for data-driven programming. In data-driven programming, program statements describe the data to be matched and the processing required rather than defining a sequence of steps to be taken.

Omlang consists of two orthogonal types:

* `variable`
* `command`

```python
 color = red + green + blue
|_____| |__________________|
command      variables
```

Where a `command` is the equivalent of a Python property; directly assignable but with programmable response/action. A `command` is not persistent and does therefore not exist on disk. A `variable` however exists on disk and is accessible with `omlang` by name.

### Nested variables

Variables in Omlang are hierarchical; meaning they may be nested within other variables. Accessing nested variables follows the same conventions a accessing individual nested members within a file-system.

```python
# Variables and values
content
|-- description
    |-- weight
    |-- height
```

Which is then used like this:

```python
# Logic
bmi = description/weight / (description/height ** 2)
```

### Current working directory & breadth-first search

Omlang revolves around the current working directory. Variables not directly available from the current working directory is searched, depth-first, through the contained hierarchy.

```bash
# Hierarchy
cwd
|-- red
|-- green
|-- parent
    |-- blue
```

```bash
# omlang
color = red + green + blue
```

Here, `blue` isn't found directly within `cwd` and is resolved into using `parent/blue` instead.