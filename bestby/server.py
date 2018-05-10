import cherrypy
import cherrypy_cors
from recipes import Recipes



if __name__ == "__main__":
    cherrypy_cors.install()
    cherrypy.tree.mount(Recipes(), '/recipes', {
        "/": {
            "request.dispatch": cherrypy.dispatch.MethodDispatcher(),
            "cors.expose.on": True,
            "cors.preflight.on": True,
            "cors.preflight.allowed_methods": ["GET", "POST", "DELETE", "PUT"]
        }
    })
    cherrypy.engine.start()
    cherrypy.engine.block()


