# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463650160.0090985
_enable_loop = True
_template_filename = '/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/eruptions.html'
_template_uri = 'eruptions.html'
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
        eruptions = context.get('eruptions', UNDEFINED)
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
        eruptions = context.get('eruptions', UNDEFINED)
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container">\r\n    <div class="row">\r\n        <div class="panel-heading"></div>\r\n        <div class="col-md-6">\r\n          <table class="table table-bordered">\r\n            <thead>\r\n              <tr>\r\n                <th>Identifiant</th>\r\n                <th>Libellé</th>\r\n                <th>Durée</th>\r\n                <th>Date</th>\r\n                <th>Intensité</th>\r\n              </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for eruption in eruptions:
            __M_writer('              <tr>\r\n                <td rowspan="2">')
            __M_writer(str(eruption.id))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(eruption.libelle))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(eruption.duree))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(eruption.date))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(eruption.intensite))
            __M_writer('</td>\t\t\t\t\r\n              </tr>\r\n')
        __M_writer('            </tbody>\r\n          </table>\r\n        </div>\r\n\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 25, "65": 25, "66": 28, "35": 2, "40": 34, "46": 3, "59": 22, "72": 66, "53": 3, "54": 19, "55": 20, "56": 21, "57": 21, "58": 22, "27": 0, "60": 23, "61": 23, "62": 24, "63": 24}, "source_encoding": "utf-8", "filename": "/users/lpro/casir/dichtelj/Bureau/ProjetPersoPython/Views/templates/eruptions.html", "uri": "eruptions.html"}
__M_END_METADATA
"""
