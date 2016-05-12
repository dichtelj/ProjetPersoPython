# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463050087.7093356
_enable_loop = True
_template_filename = '/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/eruptions_create.html'
_template_uri = 'eruptions_create.html'
_source_encoding = 'utf-8'
_exports = ['container']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def container():
            return render_container(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'container'):
            context['self'].container(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <form action="/eruption/add/" method="post">\r\n        <div class="form-group">\r\n            <label for="libelle">Libellé :</label>\r\n            <input type="text" class="form-control" id="libelle" name="libelle">\r\n            <label for="duree">Durée :</label>\r\n            <input type="text" class="form-control" id="duree" name="duree">\r\n            <label for="date">Date :</label>\r\n            <input type="text" class="form-control" id="date" name="date">\r\n            <label for="intensite">Intensité :</label>\r\n            <input type="text" class="form-control" id="intensite" name="intensite">\r\n        </div>\r\n        <input type="submit" class="btn btn-success">\r\n    </form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "eruptions_create.html", "line_map": {"56": 50, "34": 2, "27": 0, "44": 3, "50": 3}, "filename": "/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/eruptions_create.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
