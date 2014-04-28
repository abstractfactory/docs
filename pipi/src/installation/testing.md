### Testing

Look at you go! However be warned, this page is only really appreciated if you run into hassle, so feel free to skip ahead to more interesting things for now. See ya!

### [`Configuring Pipi ->`](../../configuration/overview)

### Willywork

![](https://dl.dropbox.com/s/6mvusemwwvc7omi/testing.png)

```bash
$ python .\piapp\willywork\main.pyw
```

Where `.\` refers to where `pip` installed Pipi; most commonly the site-packages of your Python installation. 

```bash
c:\Python27\Lib\site-packages\piapp
```

### Dependencies

`Willywork` is a debug application to test whether everything went well with the installation.

For convenience, all dependencies to Pipi have been encapsulated within a package called `pidep`. If you would rather use your own dependencies, remove `pidep` from your installation and refer to these packages instead.

* [`link` Open Metadata][Open Metadata] 0.5
* [`link` PyQt5][PyQt5] Built using Qt 5.1.1
* [`link` PyZMQ][PyZMQ] Built using libzmq 4.0.3
* [`link` Msgpack][Msgpack] 0.4.1

### What happened?

Congratulations, I will assume that nothing went wrong and you're now looking at Willywork, telling you he is hard at work. At this point, you've got four (or three) new packages, sprinkled with sunshine, in your Python 2.7 site-packages.

If anything is troubling you at this point, [let's talk][usergroup]. Otherwise, [let's talk][usergroup]! :D

### [`Configuring Pipi ->`](../../configuration/overview)

[devinst]: ../developer-installation
[usergroup]: https://groups.google.com/forum/#!forum/pipi-beta1
[Open Metadata]: https://github.com/abstractfactory/openmetadata
[PyQt5]: http://www.riverbankcomputing.co.uk/software/pyqt/download5
[PyZMQ]: http://zeromq.org/bindings:python
[Msgpack]: http://msgpack.org/