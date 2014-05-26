### Source Code

Store source-code with Open Metadata.

#### Potential use

```bash
$ cd /projects/hulk
```

This directory contains a flag.

```bash
$ om hidden @Flag
```

This directory also contains a pattern definition, a function for how to filter the given content.

```python
@pifou.lib.Process.cascading
def post_hide_hidden(node):
    """Hide `hidden` elements"""
    hidden = node.data('library', 'hidden')
    if not hidden:
        return node
```

* See also [Omlang](../omlang)
* See also [Open Metadata-cli](../cli)
* See also [stored procedures][storedproc]
* See also [user-defined function][udf]

### Note to self

How can we store this information using Open Metadata, in a programming-agnostic manner? Should we prefer programming-specific code? Both?

In some cases, programming-specific is better as it's known and directly compatible with the target use.

I other cases, such as the above, the code defines a pattern. Not very complex and potentially transferrable to other languages.

Both might be the way to go.

[storedproc]: http://en.wikipedia.org/wiki/Stored_procedure
[udf]: http://en.wikipedia.org/wiki/User_defined_function
[rfc61]: http://rfc.abstractfactory.io/spec/61