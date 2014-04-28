### Sorry for the hassle. :(

You may have encountered some of these issues.

> `pip` wasn't found on your `PATH`

The installer is using [`pip`][pip] and [`git`][git] to install. If you are looking to install Pipi in another directory, consider using [virtualenv][].

Given you installed `pip` as per [the guide][pip], you may have chosen to install it someplace other than the the default Python directory; e.g. by using a different Python interpreter to run the installation, such as when using `virtualenv` or the like.

That's cool. You just need to make sure it is visible via your terminal.

See [Adding Executables to your `PATH`][PATH] for more details on this.

> `git` wasn't found on your `PATH`

Sometimes running the installer directly from your browser can limit the script from accessing your file-system. Before trying anything else, try running the script from your file-browser or terminal.

If that doesn't work, the it might not be visible from your PATH.

When [installing `git`][git], you were given an option to have `git` be accessible via your terminal, or "Command Prompt". If you didn't check that, you will have to make it available yourself.

See [Adding Executables to your `PATH`][PATH] for more details on this.

> `ImportError: DLL load failed: The specified module could not be found.`

Ensure that you properly installed the [Visual C++ Redistributable][redist].


[redist]: ../installing-redist
[PATH]: ../adding-to-path
[git]: ../installing-git
[pip]: ../installing-pip