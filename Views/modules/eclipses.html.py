# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463650160.0226707
_enable_loop = True
_template_filename = '/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/eclipses.html'
_template_uri = 'eclipses.html'
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
        eclipses = context.get('eclipses', UNDEFINED)
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
        eclipses = context.get('eclipses', UNDEFINED)
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <div class="row">\r\n        <div class="panel-heading"></div>\r\n        <div class="col-md-6">\r\n          <table class="table table-bordered">\r\n            <thead>\r\n              <tr>\r\n                <th>Identifiant</th>\r\n                <th>Libellé</th>\r\n                <th>Date de début</th>\r\n                <th>Date de fin</th>\r\n                <th>Pays</th>\r\n                <th>Département</th>\r\n\t\t<th>Type</th>\r\n              </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for eclipse in eclipses:
            __M_writer('              <tr>\r\n                <td rowspan="2">')
            __M_writer(str(eclipse.id))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(eclipse.libelle))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(eclipse.dateDeb))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(eclipse.dateFin))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(eclipse.pays))
            __M_writer('</td>\t\r\n                <td>')
            __M_writer(str(eclipse.departement))
            __M_writer('</td>\t\r\n                <td>')
            __M_writer(str(eclipse.type))
            __M_writer('</td>\t\t\t\t\r\n              </tr>\r\n')
        __M_writer('            </tbody>\r\n          </table>\r\n        </div>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 27, "65": 27, "66": 28, "67": 28, "68": 29, "69": 29, "70": 32, "76": 70, "27": 0, "35": 2, "40": 37, "46": 3, "53": 3, "54": 21, "55": 22, "56": 23, "57": 23, "58": 24, "59": 24, "60": 25, "61": 25, "62": 26, "63": 26}, "source_encoding": "utf-8", "filename": "/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/eclipses.html", "uri": "eclipses.html"}
__M_END_METADATA
"""
