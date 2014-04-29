### Setting up Dashboard

![](https://dl.dropbox.com/s/lhz9qa3qlmmheue/videoplaceholder.png)

### Lovely `rootDir`

Dashboard relies on displaying a limited set of options for your artists. The starting-point of these options lie in your `rootDir`.

```
$ mkdir c:\studio
```

As good as any. For tinkering, I'd recommend making a new hierarchy someplace. Down the line, this is where you host all of your content. But for now, let's populate it something to tinker with.

```
# Content to tinker with
$ cd c:\studio
$ mkdir content\jobs
$ cd content\jobs
$ mkdir spider-man
$ mkdir star-wars
$ mkdir hulk
$ cd hulk
$ mkdir shot1
$ mkdir shot2
$ mkdir shot3

# The resulting hierarchy will look like this
studio
	content
		jobs
			spider-man
			star-wars
			hulk
				shot1
				shot2
				shot3
```

### Educate your OS

Get ready, this is about to be your first configuration, as we will finally get to see what `About` is all about. (pun)

* Right-click on your user and `Open in About`

```
# Most commonly located here
$ c:\users\marcus
```

1. Add a `rootDir` entry
2. In the `rootDir` editor, type `c:\studio`

> If you make a mistake, hit the `delete` key to remove an entry and try again.

This is what you should be ending up with.

![](https://dl.dropbox.com/s/qxutdk19croorax/rootDir.png)

### A shorter cut

I don't know about you, but if it were me, I'd have the executable of Dashboard close-by. How about we add a shortcut to our taskbar?

* Create a shortcut to `pythonw.exe`, most commonly located in `c:\python27\pythonw.exe`
* In its properties, add the full path of /piapp/dashboard/bin/dashboard.pyw

```
# For example
$ c:\python27\python.pyw C:\Python27\Lib\site-packages\piapp\dashboard\bin\dashboard.pyw
```

* Now drag this shortcut to your taskbar, or wherever you'd like it to be.

![](https://dl.dropbox.com/s/6foo41ebzkwvum9/adding-to-taskbar.png)

### [`Registering software ->`](../registering-software)

[metadata-pipi]: https://dl.dropbox.com/s/v3vc7a8p6mi2euu/metadata-pipi.png
[metadata-rootdir]: https://dl.dropbox.com/s/kde00zqccwfj15a/metadata-rootdir.png
[metadata-studio]: https://dl.dropbox.com/s/yief4pt7fiw42f3/metadata-studio.png
[PATH]: ../../installation/adding-to-path