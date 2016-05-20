# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463650159.9926586
_enable_loop = True
_template_filename = '/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/base.html'
_template_uri = 'base.html'
_source_encoding = 'utf-8'
_exports = ['container']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def container():
            return render_container(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n  <head>\r\n    <meta charset="utf-8">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1">\r\n\r\n    <title>Projet Personnel : site d\'astronomie</title>\r\n\r\n    <!-- Bootstrap core CSS -->\r\n    <link href="/Views/css/bootstrap.min.css" rel="stylesheet">\r\n\r\n    <!-- Custom styles for this template -->\r\n    <link href="/Views/css/starter-template.css" rel="stylesheet">\r\n\r\n    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->\r\n    <!--[if lt IE 9]>\r\n      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>\r\n      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>\r\n    <![endif]-->\r\n  </head>\r\n\r\n  <body>\r\n\r\n    <nav class="navbar navbar-inverse navbar-fixed-top">\r\n      <div class="container">\r\n        <div class="navbar-header">\r\n          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\r\n            <span class="sr-only">Toggle navigation</span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n          </button>\r\n          <a class="navbar-brand" href="/eclipses/">Site d\'astronomie</a>\r\n        </div>\r\n        <div id="navbar" class="collapse navbar-collapse">\r\n          <ul class="nav navbar-nav">\r\n            <li class="active"><a href="/eclipses/">Eclipses</a></li>\r\n            <li><a href="/eruptions/">Eruptions</a></li>\r\n            <li><a href="/evenements/">Autres évènements</a></li>\r\n\t\t\t<li class="dropdown">\r\n\t\t\t\t<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"\r\n\t\t\t\t   aria-expanded="false">Création<span class="caret"></span></a>\r\n\t\t\t\t<ul class="dropdown-menu">\r\n\t\t\t\t\t<li><a href="/eclipses/new/">Création eclipse</a></li>\r\n\t\t\t\t\t<li><a href="/eruptions/new/">Création éruption</a></li>\r\n\t\t\t\t\t<li><a href="/evenements/new/">Création autre évènement</a></li>\r\n\t\t\t\t</ul>\r\n\t\t\t</li>\r\n          </ul>\r\n        </div>\r\n      </div>\r\n    </nav>\r\n\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'container'):
            context['self'].container(**pageargs)
        

        __M_writer('\t\r\n\r\n    <!-- Bootstrap core JavaScript\r\n    ================================================== -->\r\n    <!-- Placed at the end of the document so the pages load faster -->\r\n    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>\r\n    <script src="/Views/js/bootstrap.min.js"></script>\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "34": 54, "23": 2, "40": 54, "28": 55, "46": 40}, "source_encoding": "utf-8", "filename": "/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/base.html", "uri": "base.html"}
__M_END_METADATA
"""
