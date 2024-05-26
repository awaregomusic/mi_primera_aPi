#importamos el modulo resource de la libreria flask_restful
from flask_restful import Resource

lista_objetos_almacen = ['lapiz', 'goma', 'pluma']

#creamos una clase que va a heredar atributos del modulo resource
class HelloWorld(Resource):

    #este metodo se va a ejecutar cuando el usuario acceda a cierta ruta a 
    def get(self):
        #regresarnos un diccionario con el mensaje que queremos mostrar
        return {"message": 'hola mundo desde la API', "status": 200}

class Almacen(Resource):
    def get(self):
        return { 'Objetos': lista_objetos_almacen, 'status' : 200}

#creamos una clase que va a manejar todas las rutas
class APIRoutes:
    #se declara un metodo para inicializar las rutas
    def init_routes(self, api):
        #agregamos una nueva ruta a nuestra api
        api.add_resource(HelloWorld, '/')
        api.add_resource(Almacen, '/objetos_almacen')