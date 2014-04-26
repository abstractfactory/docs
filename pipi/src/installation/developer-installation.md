
#### Kudos, you chose the way of the cool kids.

Either have a look at some videos, or follow the instructions below.

* [`video` Preparing Windows][Preparing Windows]
* [`video` Installing with `setup_pipi.py`][Installing with setup_pipi.py]

# Installing with [`setup_pipi.py`][inst]

This is what you *have*

* Windows >= 7, x64
* [`link` Visual C++ 2012 redist x64][redist]
* [`link` Python == 2.7.6, x64][python]
* [`link` pip >= 1.5.0][pip]
* [`link` git >= 1.9.0][git]

Now, download [`setup_pipi.py`][inst] and either double click it, or:

```python
$ python setup_pipi.py
```

This is what you *do*

```bash
$ python .\piapp\willywork\main.pyw
```

Where `.\` refers to where `pip` installed Pipi; most commonly the site-packages of your Python installation. 

The installer is using [`pip`][pip] and [`git`][git] to install. If you are looking to install Pipi in another directory, consider using [virtualenv][].

```bash
c:\Python27\Libs\site-packages\piapp
```

# Dependencies

`Willywork` is a debug application to test whether everything went well with the installation.

For convenience, all dependencies to Pipi have been encapsulated within a package called `pidep`. If you would rather use your own dependencies, remove `pidep` from your installation and refer to these packages instead.

* [`link` Open Metadata][Open Metadata] 0.5
* [`link` PyQt5][PyQt5] Built using Qt 5.1.1
* [`link` PyZMQ][PyZMQ] Built using libzmq 4.0.3
* [`link` Msgpack][Msgpack] 0.4.1

# What happened?

Congratulations, I will assume that nothing went wrong and you're now looking at Willywork, telling you he is hard at work.

(If not, [let's talk][usergroup]).

At this point, you've got three new packages, sprinkled with sunshine, in your Python 2.7 site-packages. (This is important, beta 1 is only guaranteed to work with Python 2.7, 64-bit, running on Windows, 7 and above)

Enjoy, and [let's talk][usergroup].

[Preparing Windows]: http://www.google.com
[Installing with setup_pipi.py]: http://www.google.com

[virtualenv]: http://www.virtualenv.org/en/latest/
[inst]: https://dl.dropbox.com/s/zzxvako3rko4zqt/setup_pipi.py
[devinst]: developer-installation
[userinst]: user-installation
[redist]: http://www.microsoft.com/en-gb/download/details.aspx?id=30679
[git]: http://git-scm.com/downloads
[python]: https://www.python.org/download/releases/2.7.6/
[pip]: http://pip.readthedocs.org/en/latest/installing.html
[usergroup]: https://groups.google.com/forum/#!forum/pipi-beta1
[Open Metadata]: https://github.com/abstractfactory/openmetadata
[PyQt5]: http://www.riverbankcomputing.co.uk/software/pyqt/download5
[PyZMQ]: http://zeromq.org/bindings:python
[Msgpack]: http://msgpack.org/