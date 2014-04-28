### Setting up Dashboard

![](https://dl.dropbox.com/s/lhz9qa3qlmmheue/videoplaceholder.png)

### Lovely `rootDir`

Dashboard relies on displaying a limited set of options for your artists. The starting-point of these options lie in your `rootDir`.

```
$ mkdir c:\studio\content\jobs
```

As good as any. For tinkering, I'd recommend making a new folder someplace. Down the line, this is where you will host all of your studios content. But for now, let's populate it with tinker-worthy gems of prosperity.

```
$ cd c:\studio\content\jobs
$ mkdir spider-man
$ mkdir star-wars
$ mkdir hulk
$ cd hulk
$ mkdor shot1
$ mkdor shot2
$ mkdor shot3
```

### Per-user metadata with `About`

![](https://dl.dropbox.com/s/qxutdk19croorax/rootDir.png)

Ah, finally we get to see what `About` is all about. (pun)

1. Right-click on your user and `Open in About`
```
$ c:\users\marcus
```
2. Add a new entry called `pipi`, use shift-enter to finish.
3. Inside of `pipi`, add `rootDir`, no shift this time.
4. Inside of `rootDir`, type `c:\studio`

* Note; There is a known bug with shift-enter. If you find shift not making any difference, delete the misbehaving entry by hitting `delete`, and try again.

### Per-OS environment variable

Alternatively, you may set an environment variable.

1. Add `ROOTDIR`
2. Set `ROOTDIR` to where your `rootDir` is located.

See [Adding Executables to your `PATH`][PATH] for more details on how to accomplish this.

### A shorter cut

I don't know about you, but if it were me, I'd have the executable of Dashboard close-by. How about we add a shortcut to our taskbar?


### [`Registering software ->`](../registering-software)

[PATH]: ../../installation/adding-to-path