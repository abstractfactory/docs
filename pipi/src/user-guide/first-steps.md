#### First steps

So, you've got everything up and running, huh? Well done.

Let's get down to funky snazz. 

```
The following is meant to be read from top-to-bottom, but if are familiar, then do skip ahead.
```

### Welcome About into your family

![](https://dl.dropbox.com/s/8ydcdwdbejasfim/about.JPG)

About is at the epicentre of Pipi. With it, you configure everything from the description of yourself, to the cascading results of a hierarhical software configuration.

Let's give About a warm welcome, shall we?

```
$ cd /piapp/about/bin/
$ python windows_contextmenu.py
```

This will generate a registry patch that will in turn append About to the context menu of your directory right-clicks.

```
$ windows_contextmenu.reg
```

The right-click mechanism is the main method of interacting with metadata associated to your folders from outside of Pipi and used mainly as a means of configuring big-picture stuff. (Unfortunately, for this beta, this is also the only method of interacting with metadata from outside of Pipi.)

Which we will do next!

### About has a brother

![](https://dl.dropbox.com/s/f5hthdabkebcu9e/dashboard.JPG)

Dashboard is the entry-point for artists. Much like any file-browser, it provides you with a view into your file-system. Unlike any file-browser however, it facilitates tasks and workspaces.

#### Dashboard needs a `root directory`.

This is commonly where you store all content relevant to your studio, including projects and user sandboxes.

There are two methods of telling Dashboard about this `root directory`

#### Either set user-dependent metadata with about

1. Right-click on your user and "Open in About"
```
$ c:\users\marcus
```
2. Add a folder called "pipi", without the citation marks, using shift-enter.
3. Add a "rootDir" entry within "pipi"
4. Specify where your `root directory` is located.

* Note; There is a known bug with shift-enter. If you find shift not making any difference, delete the misbehaving entry by hitting `delete`, and try again.

#### Or set an environment variable

1. Add ROOTDIR
2. Set ROOTDIR to where your `root directory` is located.
