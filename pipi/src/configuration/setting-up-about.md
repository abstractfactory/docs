### Setting up `About`

![](https://dl.dropbox.com/s/cj16fg8z24pq9u3/setting-up-about.png)

Configuration diverges into `About`. You'll configure all sorts of things here. Everything, in fact. You'll configure everything in `About`, so get cozy and let's go.

```
$ python /piapp/about/bin/windows_contextmenu.py
```

About, in fact, is so important that we will spend a moment to educate the operating system about its presence.

To do this, we will generate a `registry modification` with reference to the `About` executable; `piapp/about/bin/about.pyw`. This modification will append this executable onto your right-click menu.

If you would rather not dilute your right-click options, see here for instructions on how to perform the tasks (that you would be missing out on) by hand.

* [`guide` Manual Configuration](../using-openmetadata)

Otherwise, run the `.reg` file, confirm with Windows that this is what you want and that is it. Well done! *\*pat on back*\*

![](https://dl.dropbox.com/s/zvd15c2kgi1piy4/setting-up-about2.png)

### Removing the context menu item

Change your mind? No need to fret. If you look within the `.reg` file, you will notice two entries; one within the other. Remove the parent from your registry and all is well with the world.

Tricky monkey-business? [let's talk][usergroup]

### [`Setting up Dashboard ->`](../setting-up-dashboard)

[usergroup]: https://groups.google.com/forum/#!forum/pipi-beta1