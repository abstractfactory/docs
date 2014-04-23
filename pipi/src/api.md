# API Documentation

[The code][code] is well documented. Is not? [Let's talk.][usergroup]

# Architecture

Here is a quick overview of what layers there are, and where they fit.

The modules you have installed are each part of the Foundation layer.

* `pifou`

This is the Pipi Foundation Module, all other modules build on-top of this one. It provides the **Pipi Object Model** and **Communications Framework**, both of which are required by `pigui` and `piapp`.

* `pigui`

The Pipi GUI Module, contains all GUI objects and widgets, most of which are designed to run with PyQt5. We build software using these widgets and utilities and although each widgets stands on its own, they are without any particular intelligence. That is why you'll also need..

* `piapp`

..The Pipi Applications Module. It hosts the pre-packaged software you may come to use with Pipi. These are what your users will be most familiar with (at first) and what you might base custom software off of. Each is designed to be lightweight and extensible as they are ultimately expected to be extended by clients (that's you!).

[code]: https://github.com/abstractfactory/pifou_beta1
[usergroup]: https://groups.google.com/forum/#!forum/pipi-beta1

