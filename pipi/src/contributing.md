#### Warm and fuzzy

We encourage contributions to Pipi. If you'd like to contribute, you'll need a [GitHub][github] account and an invitation to join our [GitHub Organisation][org].

Let me know this is of interest to you, and we'll talk.

* <marcus@abstractfactory.io>

---

### Social Style

Writing code is ultimately social. Here are some guidelines for how to behave most appropriate within this codebase.

---

#### `SS1` - Don't try and solve problems that aren't directly infront of you

A side-effect of this is that you'll never attempt to complete a system all at once, but rather work only on the parts required to solve a problem at hand.

This facilitates a solution to remain minimally complete, but also relevant, as there is a chance that your optional solutions may not ever be required and may instead bog down overall clarity of a project.

---

#### `SS2` - Define a problem before solving it

By defining it, you gain perspective and the ability to communicate your ideas before committing to any one idea in particular.

Have a look at http://rfc.abstractfactory.io for examples of how we approach defining problems.

---

#### `SS3` - Keep it simple

I'll let Albert speak for himself.

> If you can't explain it simply, you don't understand it well enough. - Albert Einstein

> Make everything as simple as possible, but not simpler. - Albert Einstein

---

#### `SS4` - Third-party

* Use of third-party *ideas* are encouraged.
* Use of third-party *implementantions* are discouraged.

The motivation to this guideline is to encourage re-use of existing concepts, whilst keeping the learning curve small. Additional third-party implementations are only considered if you can illustrate the pros and cons of doing so; given that the pros outweight the cons.

---

### Coding Style

Ride in style. All code here follows PEP8 without exception.

---

#### `CS1` - Fork, submit pull-request

That sums up the gist of our collaboration.

---

#### `CS2` - Fork, don't branch

Forks are encouraged over branching. Each fork is then also encourage to be functional on it's own, but is not required to. A fork is then worked upon in isolation, similar to a branch, and finally pull-requested into the original.

---

#### `CS3` - Self-documenting

All code strives to be self-documenting/self-describing. Meaning variable names communicate their value, functions and methods communicate their actions. Part of making this feasable is keeping functions and methods concise and in an ideal world they would all be atomic; i.e. not causing side-effects, not touching anything outside of their input arguments.

---

#### `CS4` - Doctest

Doc-tests are the main vessel of ensuring code-health. The following module has been crafted to illustrate how self-documenting code should look, with an ideal amount of doctests.

[path.py](https://github.com/abstractfactory/openmetadata/blob/master/openmetadata/path.py)

---

#### `CS5` - Standalone modules

All modules MUST be executable on its own. This means, amonst other things, no relative imports and no mutating of global scope; such as appending features to native `os` or `sys` modules.

---
	
#### `CS6` - Cyclic dependency

As a side-effect of the above, Standalone modules, there MUST NOT be any cyclic dependencies.

#### `CS7` - Name clashing

Name clashes are resolved using a underscore suffix.

E.g.

```python
name1 = 'hello'
name1_ = 'world'
```

### GUI

* The main graphical framework in use is Python binding of Qt version 5.2.1 called PyQt5.
* All styling is done via CSS and as such each stylable widget MUST provide an `objectName` so as to be accessible via CSS.

As each widget maintains an `objectName` they no longer require an instance variable for persistence.

```python
mywidget = QtWidgets.QWidget()
mywidget.setObjectName('MyWidget')  # Node: Object names MUST use MixedCase

# Widget is now accessible from both CSS and code
```

**style.css**

```css
#MyWidget {
	background-color: blue;
}
```

**style.py**

```python
mywidget = self.findChild(QtWidgets.QWidget, 'MyWidget')
```

The main motivation for discarding instance variables is to reduce errors and misunderstandings. Ultimately, providing both an object name AND and instance variable of the same object is duplicity and thus violates the DRY principle.

```python
# This is an instance variable, and it is not encouraged.
self.mywidget = mywidget
```


[usergroup]: https://groups.google.com/forum/#!forum/pipi-beta1
[PEP8]: http://legacy.python.org/dev/peps/pep-0008/
[github]: http://github.com
[org]: https://github.com/abstractfactory