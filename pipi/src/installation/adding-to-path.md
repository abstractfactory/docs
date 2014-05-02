### Adding Python to your `PATH`

Adding Python, any executable really, is a matter of appending a directory to an environment variable known as `PATH`.

Note that programs won't see a change in environment until it has been restarted. This is the same for any platform.

#### Windows

On Windows, you could use the `setx` command to accomplish this.

`A)` If you haven't got a PATH setup yet:

```
$ setx PATH c:\Python27

SUCCESS: Specified value was saved.

```

`B)` Otherwise, you may add to your existing PATH

```
$ setx PATH "%PATH%;c:\Python27"

SUCCESS: Specified value was saved.

```

For any other executable, locate the directory in which the executable resides, and add that to your PATH, as shown above.

