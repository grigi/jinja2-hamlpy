Jinja2-HamlPy
=============

HamlPy extension for Jinja2.

Basic Usage
-----------
To use this extension you just need to add it to you jinja environment and use ".haml" as extension for your templates.

::

  from jinja2 import Environment
  from jinja2_hamlpy import HamlPyExtension
  
  env = Environment(extensions=[HamlPyExtension])

For Coffin Users:
-----------------
Simply add this to your settings::

  JINJA2_EXTENSIONS = [
      'jinja2_hamlpy.HamlPyExtension',
  ]

