# Tutorial

Reference: http://api.mongodb.org/python/current/tutorial.html

This tutorial is intended as an introduction to working with Open Metadata using Python.

### Prerequisites

Before we start, make sure that you have the Open Metadata distribution [installed.][install] In the Python shell, the following should run without raising an exception:

```python
>>> import openmetadata
```

Open Metadata is de-centralised, which means that as opposed to a regular database such as MongoDB, you won't need a central server running to use it. (although you should and probably want to; I'll explain why in a bit).

### Hello World

To get started, we will create a string attribute in your home folder containing the words "Hello World".

```python
path = '/home/marcus'
location = openmetadata.Location(path)
test_entry = openmetadata.Entry('test_entry', data='Hello World', parent=location)
```

The above code will associate 'test_entry' with our home directory. Remember, Open Metadata creates entries lazily; no data is actually written to disk yet.

### Writing to disk

Databases are inherently central and store all data within one location on your file-system. Conversely, Open Metadata is de-centralised and stores your data in files right next to the folder you associate it with.

```python
>>> openmetadata.flush(location)
```

The above code will "flush" all associated data for our home directory. At this point, here is what your home directory will look like:

```bash
cat /home/marcus/.meta/test_entry.string
Hello World
```

This file then contains the JSON-encoded string, "Hello World"

### Bulk write

[install]: https://github.com/abstractfactory/openmetadata