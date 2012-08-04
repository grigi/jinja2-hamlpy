Jinja2-HamlPy
=============

HamlPy extension for Jinja2 adapted from Djinja

Basic Usage
-----------
To use this extension you just need to add it to you jinja environment and use ".haml" as extension for your templates.

::

  from jinja2 import Environment
  import jinja2_hamlpy
  
  env = Environment(extensions=[jinja2_hamlpy])

For Coffin Users:
-----------------
Simply add this to your settings::

  JINJA2_EXTENSIONS = [
      'jinja2_hamlpy',
  ]

