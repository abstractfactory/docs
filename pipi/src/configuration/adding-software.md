### Adding software

![](https://dl.dropbox.com/s/lhz9qa3qlmmheue/videoplaceholder.png)

### Per-folder basis

All software is installed and configured on a per-project basis. Or rather, a per-folder basis. Each software is then compounded by children within the hierarchy; look.

```
hulk
	softwareX
	shot1
		softwareY
```

Here, `hulk` has `softwareX` installed throughout the whole project. However, `shot1` has an additional software installed. Perhaps one with only a limited set of licenses available, only really needed within this one task. As an end-result, workers of `shot1` will have the option of working in either `softwareX` or `softwareY`

### Schema

The convention is this:

```
folder
	appdata
		{key}.app
```

Any folder installed with software contains `appdata`. `appdata` then contains a `key` per installed software; suffixed with `.app` More on `appdata` and the 3 other distinct layers of configurable content in [RFC31][]

### Remember your training, Luke

In the [previous guide](../registering-software) we associated a name to a specific application; `calc`. That is our `key`.

```
folder
	appdata
		calc.app
```

`appdata` is then used as a container for each installed application into `folder`.

### Success

You made it! I am so proud of you. :) Now on you go!

### [`Adding a new workspace ->`](../adding-new-workspace)

[RFC31]: http://rfc.abstractfactory.io/spec/31/