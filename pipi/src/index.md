<!-- ![](../img/company.png) -->
![](https://dl.dropbox.com/s/o3s62jqkn1c51lg/title.png)

Abstract Factory Ltd.
Copyright 2014

# Usergroup

First things first, if you have any question, suggestions or just want to spread the love, head over to the

[**Pipi Beta 1 - Usergroup**][usergroup]

Now fly little bird, fly!

Videos

* 

# Installing with `pip`

Assuming you've got a 64-bit version of Windows 7 or 8, Python 2.7 and `pip`, pop open a command prompt and type this:

```bash
$ pip install git+git://github.com/abstractfactory/pifou_beta1.git
$ pip install git+git://github.com/abstractfactory/pigui_beta1.git
$ pip install git+git://github.com/abstractfactory/piapp_beta1.git
```

(You may copy/paste) Now run Dashboard, like this:

```bash
$ python .\piapp\dashboard\bin\dashboard.pyw
```

Where `.\` refers to where `pip` installed Pipi; most commonly the site-packages of your Python installation.

# Dependencies

Dashboard may complain about missing dependencies. If so, go ahead and also install the **Pipi Dependency Module**.

```bash
$ pip install git+git://github.com/abstractfactory/pidep.git
```

For convenience, dependencies have been encapsulated within this one package. If you decide later to use your own dependencies, well, then you are free to do so. Here they are.

* Environment 		-- Windows 7 x64, Python 2.7.6 x64
* [Open Metadata][] -- v0.5
* [PyQt5][]			-- Built using Qt 5.1.1
* [PyZMQ][]		 	-- Built using libzmq 4.0.3
* [Msgpack][]		-- v0.4.1

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
[RFC31]: http://rfc.abstractfactory.io/spec/31/
[RFC24]: http://rfc.abstractfactory.io/spec/24
[RFC25]: http://rfc.abstractfactory.io/spec/25
[RFC27]: http://rfc.abstractfactory.io/spec/27
[RFC28]: http://rfc.abstractfactory.io/spec/28
[usergroup]: https://groups.google.com/forum/#!forum/pipi-beta1
[Open Metadata]: https://github.com/abstractfactory/openmetadata
[PyQt5]: http://www.riverbankcomputing.co.uk/software/pyqt/download5
[PyZMQ]: http://zeromq.org/bindings:python
[Msgpack]: http://msgpack.org/