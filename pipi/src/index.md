<!-- ![](../img/company.png) -->
![](https://dl.dropbox.com/s/x6gap4a13jekdnz/title.png)

Abstract Factory Ltd.
Copyright 2014

# Usergroup

First things first, if you have any question, suggestions or just want to spread the love go here:

[**Usergroup**][usergroup]

Now fly little bird, fly!

* [`video` Installing with `pip`][Installing with pip]
* [`video` Running Software][Running Software]
* [`video` Adding a new workspace][Adding a new workspace]
* [`video` Adding software][Adding software]
* [`video` Registering software][Registering software]
* [`video` Configuring Software][Configuring Software]
* [`video` Non-available software][Non-available software]

# Installing with [`pip`][pip]

This is what you *have*

* Windows >= 7, x64
* [`link` Visual C++ 2012 redist x64][redist]
* [`link` Python == 2.7.6, x64][python]
* [`link` pip >= 1.5.0][pip]
* [`link` git >= 1.9.0][git]

This is what you *run*

```bash
$ pip install git+https://github.com/abstractfactory/pifou_beta1.git
$ pip install git+https://github.com/abstractfactory/pigui_beta1.git
$ pip install git+https://github.com/abstractfactory/piapp_beta1.git
```

This is what you *do*

```bash
$ python .\piapp\dashboard\bin\dashboard.pyw
```

Where `.\` refers to where `pip` installed Pipi; most commonly the site-packages of your Python installation.

```bash
c:\Python27\Libs\site-packages\piapp
```

# Dependencies

Dashboard may complain about missing dependencies. If so, go ahead and also install the **Pipi Dependency Module**.

```bash
$ pip install git+git://github.com/abstractfactory/pidep.git
```

For convenience, dependencies have been encapsulated within this one package. If you decide later to use your own dependencies, well, then you are free to do so. Here they are.

* [`link` Open Metadata][Open Metadata] v0.5
* [`link` PyQt5][PyQt5] Built using Qt 5.1.1
* [`link` PyZMQ][PyZMQ]  Built using libzmq 4.0.3
* [`link` Msgpack][Msgpack] v0.4.1

# What happened?

Congratulations, I will assume that nothing went wrong and you're now looking at Dashboard, the entry-point for artists. (If not, [let's talk][usergroup]).

At this point, you've got three new packages, sprinkled with sunshine, in your Python 2.7 site-packages. (This is important, beta 1 is only guaranteed to work with Python 2.7, 64-bit, running on Windows, 7 and above)

# More

You got it!

* [Specification][RFC23]
* [Requirements][RFC25]
* [Architecture][RFC27]
* [Metadata][RFC24]
* [Configurable Content][RFC31]
* [FAQ][RFC28]

Open Metadata

* [RFC10][]: Open Metadata Specification
* [RFC12][]: Cascading
* [RFC13][]: Task Distribution
* [RFC14][]: Temporal Metadata
* [RFC15][]: Meta Metadata
* [RFC16][]: Blob
* [RFC17][]: Cross-referencing
* [RFC18][]: Types
* [RFC19][]: Storage Agnostic
* [RFC20][]: Referencing
* [RFC35][]: Garbage Collectio[]
* [RFC41][]: Driver
* [RFC46][]: Temporal Resolution



[RFC10]: http://rfc.abstractfactory.io/spec/10
[RFC12]: http://rfc.abstractfactory.io/spec/12
[RFC13]: http://rfc.abstractfactory.io/spec/13
[RFC14]: http://rfc.abstractfactory.io/spec/14
[RFC15]: http://rfc.abstractfactory.io/spec/15
[RFC16]: http://rfc.abstractfactory.io/spec/16
[RFC17]: http://rfc.abstractfactory.io/spec/17
[RFC18]: http://rfc.abstractfactory.io/spec/18
[RFC19]: http://rfc.abstractfactory.io/spec/19
[RFC20]: http://rfc.abstractfactory.io/spec/20
[RFC35]: http://rfc.abstractfactory.io/spec/35
[RFC41]: http://rfc.abstractfactory.io/spec/41
[RFC46]: http://rfc.abstractfactory.io/spec/46
[RFC23]: http://rfc.abstractfactory.io/spec/23
[RFC31]: http://rfc.abstractfactory.io/spec/31
[RFC24]: http://rfc.abstractfactory.io/spec/24
[RFC25]: http://rfc.abstractfactory.io/spec/25
[RFC27]: http://rfc.abstractfactory.io/spec/27
[RFC28]: http://rfc.abstractfactory.io/spec/28

[Installing with pip]: http://www.google.com
[Running Software]: http://www.google.com
[Adding a new workspace]: http://www.google.com
[Adding software]: http://www.google.com
[Registering software]: http://www.google.com
[Configuring Software]: http://www.google.com
[Non-available software]: http://www.google.com

[redist]: http://www.microsoft.com/en-gb/download/details.aspx?id=30679
[git]: http://git-scm.com/downloads
[python]: https://www.python.org/download/releases/2.7.6/
[pip]: http://pip.readthedocs.org/en/latest/installing.html
[usergroup]: https://groups.google.com/forum/#!forum/pipi-beta1
[Open Metadata]: https://github.com/abstractfactory/openmetadata
[PyQt5]: http://www.riverbankcomputing.co.uk/software/pyqt/download5
[PyZMQ]: http://zeromq.org/bindings:python
[Msgpack]: http://msgpack.org/