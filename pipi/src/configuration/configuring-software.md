### Configuring software

![](https://dl.dropbox.com/s/lhz9qa3qlmmheue/videoplaceholder.png)

### Time for your reward

I bet you're pretty stumped by now. Having gone through all of these guides.. for what? To start `notepad`? No no no.

The first thing we need to do, is move away from `notepad`. It isn't worthy of the awesum-sauce we are about to sprinkle upon our software. We are about to configure the manner in which software is launched. But first, let's educate ourselves about some fundamentals of software configuration.

### Args and Kwargs

Highly-configurable software sometimes enable you to run it with a pre-determined set of options; `flags`. In programming-land, there is a similar concept to `flags` called `arguments` or `parameters`, often shortened to `args`. `args` are value-less keys; meaning they only contain a name. Their complement, `kwargs`, stands for key-word arguments and contains both a name, and a value; a.k.a. `key/value pair`.

```
# Running software with args
c:\program files\autodesk\maya2014\bin\maya.exe -hideConsole

# Running software with kwargs
c:\program files\autodesk\maya2014\bin\maya.exe -proj c:\studio\hulk\shot5

```

### Environment

Some software utilise your environment. For such software, you may be interested in bending this environment to suit your needs. The environment may be modified in such a way that the only one making use of it, is your executed software.

```
$ set PYTHONPATH=c:\studio\content\jobs\hulk\appdata\maya.app\scripts
$ maya
```

There. We're running `Maya`, using our modified environment.

### Configuring with Pipi

You knew it would come to this. :) The Pipi-equivalent of above actions looks like this.

```
>>> import os
>>> import openmetadata
>>>
>>> # Gather data
>>> maya = r'c:\studio\content\jobs\hulk\appdata\maya.app'
>>> workspace = r'c:\studio\content\jobs\hulk\shot5'
>>> PYTHONPATH = os.path.join(maya, 'scripts')
>>>
>>> # Finally, record our changes into our installed software
>>> openmetadata.write(maya, 'args\-hideConsole.flag')
>>> openmetadata.write(maya, 'kwargs\-proj', workspace)
>>> openmetadata.write(maya, 'environment\PYTHONPATH', PYTHONPATH)
```

If you are uncomfortable with looking at code, have a look at the video above for how this is done using About.

### Meatball and pasta

And that is it. The next time you run `Maya` from Dashboard, it will be without a console, running under your specified `workspace` and including our modified environment.

### [`Non-available software ->`](../non-available-software)