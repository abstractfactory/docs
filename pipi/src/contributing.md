#### Warm and fuzzy

We encourage contributions to Pipi. If you'd like to contribute, you'll need a [GitHub][github] account and an invitation to join our [GitHub Organisation][org].

Let me know this is of interest to you, and we'll talk.

* <marcus@abstractfactory.io>

### Fork, submit pull-request

That sums up the gist of our collaboration.

---

# Style guide

Ride in style. All code here follows PEP8 without exception.

### Self-documenting

All code strives to be self-documenting/self-describing. Meaning variable names communicate their value, functions and methods communicate their actions. Part of making this feasable is keeping functions and methods concise and in an ideal world they would all be atomic; i.e. not causing side-effects, not touching anything outside of their input arguments.

#### Doctest

The code-base is nimble and agile. Doc-tests are currently the main vessel of ensuring code-health. The following module has been crafted to illustrate how self-documenting code should look, with an ideal amount of doctests.

[path.py](https://github.com/abstractfactory/openmetadata/blob/master/openmetadata/path.py)

#### Standalone modules

All modules MUST be executable on its own.

#### Cyclic dependency

As a consequence of the above, Standalone modules, there MUST NOT be any cyclic dependencies.

[usergroup]: https://groups.google.com/forum/#!forum/pipi-beta1
[PEP8]: http://legacy.python.org/dev/peps/pep-0008/
[github]: http://github.com
[org]: https://github.com/abstractfactory