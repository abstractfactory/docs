#### Let's get going

Have a look at some videos, see below for nitpicks of information, and [don't forget to talk][usergroup] about things on your mind.

* [`video` Running Software][Running Software]
* [`video` Adding a new workspace][Adding a new workspace]
* [`video` Adding software][Adding software]
* [`video` Registering software][Registering software]
* [`video` Configuring Software][Configuring Software]
* [`video` Non-available software][Non-available software]

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

#### Cascading appdata

Application configuration should be adding to existing configuration up a hierarchy, but currently does not. Instead, it replaces any previous configuration.

```python
# Example here..

```

### Next

#### [First steps with Pipi -->][firststeps]

[firststeps]: user-guide/firststeps
[usergroup]: https://groups.google.com/forum/#!forum/pipi-beta1
[Running Software]: http://www.google.com
[Adding a new workspace]: http://www.google.com
[Adding software]: http://www.google.com
[Registering software]: http://www.google.com
[Configuring Software]: http://www.google.com
[Non-available software]: http://www.google.com

[OMS]: http://rfc.abstractfactory.io/spec/10