
### In this version

This beta contains the most fundamental elements of a production pipeline; the part which deals with software and their configuration.

* `Configuration per-folder`
* `Cascading metadata`
* `Software discovery`
* `Software installs per-folder`
* `Software launching`

#### Supported types in About

New metadata entries defaults to string. But you may customise they datatype by specifying a suffix.

```bash
$ my_integer.int
$ my_boolean.bool
```

Here are the supported types as of this release:

* `string`
* `int`
* `float`
* `bool`

See the Open Metadata specification for full details on future support and features.

[Open Metadata Specification][OMS]

### Not in this version

This beta lacks functionality not immediately visible at first glance.

Those are

* `Cascading appdata`
* `Metadata renaming`
* `Creating/Deleting folders from Dashboard`

#### Cascading appdata

Application configuration should be adding to existing configuration up a hierarchy, but currently does not. Instead, it replaces any previous configuration.

```python
# Example here..

```
