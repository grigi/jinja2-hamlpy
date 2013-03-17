import os.path

from hamlpy.hamlpy import Compiler
from jinja2 import TemplateSyntaxError
from jinja2.ext import Extension


class HamlPyExtension(Extension):
    
    HAML_EXTENSIONS = ('.haml', )
    
    def preprocess(self, source, name, filename=None):
        if not name or os.path.splitext(name)[1] not in self.HAML_EXTENSIONS:
            return source

        compiler = Compiler()
        try:
            return compiler.process(source)
        except Exception, e:
            raise TemplateSyntaxError(e, None, name=name, filename=filename)
