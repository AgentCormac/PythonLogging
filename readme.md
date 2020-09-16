LogTest
========

Code illustrating the correct usage of logging in Python

Objectives:

* Use external configuration file
* Use multiple handlers
* Override default logging configuration for specific packages, modules (and classes).

Python logging is difficult to use (non-intuitive) mainly because the documentation is totally rubbish. Most examples show setting up logging by including code into scripts. This is plainly wrong for any application of significant worth as it means that the code has to be changed to alter the logging to enable the detection of bugs. Logging is also further complicated by Python's lax scoping rules.

Essentially my recommendations are:

* Use dictconfig for your logging configuration. For some reason it is more flexible and detailed than plain fileconfig
* Use a yaml to store your logging configuration as it is easier to read and understand.
* Set up you preferred logging options onto the root logger and then detail specific log-handlers for slasses, modules or packages as required.
* To prevent lost log messages always set up a logger on the instantiation of a class or in each callable method of a module. Do not set up a logger in te module body as this will be over-written by the main class root logger configuration.
* If all else fails logging for a 3rd party library can be turned off by directing all output from that library to a null device:
```
import annoyingLibrary
logging.getLogger('annoyingLibrary').addHandler(logging.NullHandler())
```

