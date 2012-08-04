from jinja2.ext import Extension
from jinja2 import TemplateSyntaxError
from hamlpy.hamlpy import Compiler
import os

class HamlPyExtension(Extension):
    def preprocess(self, source, name, filename=None):
        if name is None or os.path.splitext(name)[1] not in ('.haml',):
            return source

	compiler = Compiler()
        try:
            return compiler.process(source)
        except Exception, e:
            raise TemplateSyntaxError(e, None, name=name, filename=filename)

