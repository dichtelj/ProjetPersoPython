# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463650160.0360205
_enable_loop = True
_template_filename = '/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/evenements.html'
_template_uri = 'evenements.html'
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
        evenements = context.get('evenements', UNDEFINED)
        def container():
            return render_container(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'container'):
            context['self'].container(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        evenements = context.get('evenements', UNDEFINED)
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <div class="row">\r\n        <div class="panel-heading"></div>\r\n        <div class="col-md-6">\r\n          <table class="table table-bordered">\r\n            <thead>\r\n              <tr>\r\n                <th>Identifiant</th>\r\n                <th>Libellé</th>\r\n                <th>Date de début</th>\r\n                <th>Date de fin</th>\r\n                <th>Pays</th>\r\n                <th>Département</th>\r\n              </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for evenement in evenements:
            __M_writer('              <tr>\r\n                <td rowspan="2">')
            __M_writer(str(evenement.id))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(evenement.libelle))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(evenement.dateDeb))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(evenement.dateFin))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(evenement.pays))
            __M_writer('</td>\t\r\n                <td>')
            __M_writer(str(evenement.departement))
            __M_writer('</td>\t\t\t\r\n              </tr>\r\n')
        __M_writer('            </tbody>\r\n          </table>\r\n        </div>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 26, "65": 26, "66": 27, "35": 2, "68": 30, "40": 35, "74": 68, "46": 3, "59": 23, "67": 27, "53": 3, "54": 20, "55": 21, "56": 22, "57": 22, "58": 23, "27": 0, "60": 24, "61": 24, "62": 25, "63": 25}, "source_encoding": "utf-8", "filename": "/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/evenements.html", "uri": "evenements.html"}
__M_END_METADATA
"""
