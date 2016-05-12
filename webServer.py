import routes
import cherrypy
import inspect, os
from mako.template import Template
from mako.lookup import TemplateLookup
from Database.Database import Database
from Models.models import *

try:
    _curdir = os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
except NameError:
    __file__ = inspect.getfile(inspect.currentframe())
    _curdir = os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
print(_curdir)

myTemplatesDir = os.path.join(_curdir, 'Views/templates')
myModulesDir = os.path.join(_curdir, 'Views/modules')
mylookup = TemplateLookup(directories=[myTemplatesDir], module_directory=myModulesDir,
                          output_encoding='utf-8',
                          encoding_errors='replace')
# ------------------------------------------------------------
# Templates HTML
# ------------------------------------------------------------
_eruptions = mylookup.get_template("eruptions.html")
_eclipses = mylookup.get_template("eclipses.html")
_evenements = mylookup.get_template("evenements.html")

_eruptions_create = mylookup.get_template("eruptions_create.html")
_eclipses_create = mylookup.get_template("eclipses_create.html")
_evenements_create = mylookup.get_template("evenements_create.html")


class App:
    """
    Application
    """

    def eruptions(self):
        db = Database()
        eruptions = db.retrieve(Eruption)
        return _collection.render_unicode(eruptions=eruptions)

    def eclipses(self):
        db = Database()
        eclipses = db.retrieve(Eclipse)
        return _collection.render_unicode(eclipses=eclipses)

    def evenements(self):
        db = Database()
        evenements = db.retrieve(Evenement)
        return _collection.render_unicode(evenements=evenements)

class EruptionController:

    @cherrypy.expose
    def eruptions(self):
        db = Database()
        eruptions = db.retrieve((Eruption))
        return _eruptions.render_unicode(eruptions=eruptions)


    @cherrypy.expose
    def eruptions_add(self, libelle, duree, date, intensite):
        eruption = Eruption(libelle, duree, date, intensite)
        db = Database()
        db.create(eruption, Eruption)
        raise cherrypy.HTTPRedirect('/eruptions/')

    @cherrypy.expose
    def eruptions_create(self):
        db = Database()
        return _eruptions_create.render_unicode(
            eruptions=db.retrieve(Eruption)
        )

class EclipseController:

    @cherrypy.expose
    def eclipses(self):
        db = Database()
        eclipses = db.retrieve((Eclipse))
        return _eclipses.render_unicode(eclipses=eclipses)


    @cherrypy.expose
    def eclipses_add(self, libelle, dateDeb, dateFin, pays, departement, type):
        eclipse = Eclipse(libelle, dateDeb, dateFin, pays, departement, type)
        db = Database()
        db.create(eclipse, Eclipse)
        raise cherrypy.HTTPRedirect('/eclipses/')

    @cherrypy.expose
    def eclipses_create(self):
        db = Database()
        return _eclipses_create.render_unicode(
            eclipses=db.retrieve(Eclipse)
        )
    
class EvenementController:

    @cherrypy.expose
    def evenements(self):
        db = Database()
        evenements = db.retrieve((Evenement))
        return _evenements.render_unicode(evenements=evenements)


    @cherrypy.expose
    def evenements_add(self, libelle, dateDeb, dateFin, pays, departement, type):
        evenement = Eclipse(libelle, dateDeb, dateFin, pays, departement, type)
        db = Database()
        db.create(evenement, Eclipse)
        raise cherrypy.HTTPRedirect('/evenements/')

    @cherrypy.expose
    def eclipses_create(self):
        db = Database()
        return _eclipses_create.render_unicode(
            eclipses=db.retrieve(Eclipse)
        )

if __name__ == '__main__':
    global_conf = {
        'global': {'autoreload.on': False,
                   'server.socket_host': '127.0.0.1',
                   'server.protocol_version': 'HTTP/1.1',
                   'server.thread_pool': 5,
                   'tools.encode.encoding': "Utf-8",
                   'environment': 'production',
                   'log.error_file': 'site.log',
                   'log.screen': True}}
    cherrypy.config.update(global_conf)
    app = App()
    d = cherrypy.dispatch.RoutesDispatcher()
    d.connect('default_route', '/', controller=app, action='index')
    
    d.connect('eruptions', '/eruptions/', controller=app, action='eruptions')
    d.connect('eclipses', '/eclipses/', controller=app, action='eclipses')
    d.connect('evenements', '/evenements/', controller=app, action='evenements')
    
    d.connect('eruptions_create', '/eruptions/new', controller=MangaController, action="eruptions_create")
    d.connect('eruptions_add', '/eruptions/add/', controller=MangaController, action="eruptions_add")

    d.connect('eclipses_create', '/eclipses/new', controller=MangaController, action="eclipses_create")
    d.connect('eclipses_add', '/eclipses/add/', controller=MangaController, action="eclipses_add")

    d.connect('evenements_create', '/evenements/new', controller=MangaController, action="evenements_create")
    d.connect('evenements_add', '/evenements/add/', controller=MangaController, action="evenements_add")

    conf_appli = {
        '/': {'request.dispatch': d},
        '/Views': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(_curdir, 'Views')},
        '/Views/templates': {'tools.staticdir.on': True, 'tools.staticdir.dir': myTemplatesDir},
        '/Views/modules': {'tools.staticdir.on': True, 'tools.staticdir.dir': myModulesDir},
        '/Views/css': {
            'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(_curdir, 'Views/css'),
            'tools.staticdir.content_types': {'css': 'text/css'}
        },
        '/Views/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(_curdir, 'Views/js'),
            'tools.staticdir.content_types': {'js': 'application/javascript'}
        }}

    cherrypy.quickstart(app, config=conf_appli)
