# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463650160.0726118
_enable_loop = True
_template_filename = '/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/evenements_create.html'
_template_uri = 'evenements_create.html'
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
        __M_writer('\r\n<div class="container">\r\n    <form action="/evenements/add/" method="post">\r\n        <div class="form-group">\r\n            <label for="libelle">Libellé :</label>\r\n            <input type="text" class="form-control" id="libelle" name="libelle">\r\n            <label for="dateDeb">Date de début :</label>\r\n            <input type="text" class="form-control" id="dateDeb" name="dateDeb">\r\n            <label for="dateFin">Date de fin :</label>\r\n            <input type="text" class="form-control" id="dateFin" name="dateFin">\r\n            <label for="pays">Pays :</label>\r\n            <input type="text" class="form-control" id="pays" name="pays">\r\n            <label for="departement">Département :</label>\r\n            <input type="text" class="form-control" id="departement" name="departement">\r\n        </div>\r\n        <input type="submit" class="btn btn-success">\r\n    </form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"56": 50, "34": 2, "27": 0, "44": 3, "50": 3}, "source_encoding": "utf-8", "filename": "/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/evenements_create.html", "uri": "evenements_create.html"}
__M_END_METADATA
"""
