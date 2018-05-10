import cherrypy #our webserver; accept requests + dispatch to handlers
from schema.db import Session
from schema import Recipe

@cherrypy.expose()
@cherrypy.popargs("recipe_id")
class Recipes(object):

    @cherrypy.tools.json_out()
    def GET(self):
        db_session = Session()
        results = db_session.query(Recipe)
        results_array = [r.to_view() for r in results]
        db_session.close()
        return results_array

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def POST(self):
        params = cherrypy.request.json
        #validation step
        errors = []
        if not params.get('name'):
            errors.append({
                "code":"field.name.null",
                "field":"name"
            })

        if len(errors):
            cherrypy.response.status = 400
            return errors

        new_recipe = Recipe(name=params.get('name'))

        db_session = Session()
        db_session.add(new_recipe)
        db_session.commit()
        new_recipe_view = new_recipe.to_view()
        db_session.close()
        cherrypy.response.status = 201
        return new_recipe_view
#del = 204; no content

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def PUT(self, recipe_id:int):
        params = cherrypy.request.json

        if "id" in params:
            del params["id"]

        db_session = Session()
        results = db_session.query(Recipe).filter(Recipe.id == recipe_id)

        if not results.count():
            cherrypy.response.status = 404
            return {
                "code":"recipe.notfound",
                "field":"id"
            }

        results.update(params)
        update_recipe = results.one()

        db_session.commit()

        update_recipe_view = update_recipe.to_view()

        db_session.close()

        return update_recipe_view

    @cherrypy.tools.json_out()
    def DELETE(self, recipe_id:int):
        db_session = Session()
        results = db_session.query(Recipe).filter(Recipe.id == recipe_id)

        if not results.count():
            cherrypy.response.status = 404
            return {
                "code":"recipe.notfound",
                "field":"id"
            }


        results.delete()
        db_session.commit()
        db_session.close()
        cherrypy.response.status = 204

    def OPTIONS(self):
        pass

