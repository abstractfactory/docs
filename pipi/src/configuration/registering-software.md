### Registering software

![](https://dl.dropbox.com/s/lhz9qa3qlmmheue/videoplaceholder.png)

### [An application launcher][applauncher]

Dashboard is good for two things; running software and configuring the context under which that software is run. This guide will be about running software, and for that we will employ a process called [Software Discovery][softdisc]. Here, we'll employ a *de-centralised method* of software discovery; meaning that we will embark on educating our operating system about what software it has available.

### Find an executable

Step one is to locate an executable.

```
C:\Windows\calc.exe
```

As good as any. Now we will want to expose this executable. The process is identical to how we exposed Python et. al. to your terminal [earlier][PATH]. That's right, we're going to add it to our PATH.

Anything located on your PATH is accessible via a single keyword.

### Showing ya' true colors

We could add this:

```
c:\Windows
```

Now, `calc.exe` would be accessible via the terminal, but so would everything else residing in that directory. Not very minimalistic. Let's instead note the absolute path of `calc.exe` into a `.bat` file and position it in a folder that we will later expose.

```
$ mkdir c:\bin
$ echo "c:\Windows\calc.exe" > c:\bin\calc.bat
```

As good as any. Now go ahead and [add this folder to your PATH][PATH]. By doing it this way, we gain a finer level of control over what is exposed and what is not.

> `c:\Windows` is included in your PATH by default. In fact, that is how you are able to run `calc`, `calc` and so on directly from `Run..` or a terminal.

### An added benefit

Separating your executables from their original directory has an added benefit of being separated from its original name. Imagine for a second that you were running `calc 1.0` alongside `calc 2.0`. These two versions are incompatible with each other, so it is important to keep data produced by them separate.

```
$ echo "c:\Windows-7\calc.exe" > c:\bin\calc-1.0.bat
$ echo "c:\Windows-8\calc.exe" > c:\bin\calc-2.0.bat
```

Having added both of these directories to our path would have made it impossible for us to reference a specific version.

More on this later.

### [`Adding Software ->`](../adding-software)


[softdisc]: http://rfc.abstractfactory.io/spec/21/
[applauncher]: http://en.wikipedia.org/wiki/Comparison_of_desktop_application_launchers
[PATH]: ../../installation/adding-to-path