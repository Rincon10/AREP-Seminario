from flask_restful import Resource, reqparse, abort
import sys
sys.path.append(".")
from FileAnalyzer.file_analyzer import FileAnalyzer

# Configuramos los parámetros del necesarios para crear un grafo
graph_put_args = reqparse.RequestParser()
graph_put_args.add_argument("url", type=str, help="URL is required", required=True)

class FileAnalyzerApi(Resource):
    def __init__(self):
        # URL
        self._url = None

        self._data = None

    # Getters y setters
    @property
    def url(self):
        '''
        Getter de la variable 'url'.
        :return: La variable 'ur;'
        '''
        return self._url

    @url.setter
    def url(self, url):
        '''
            Setter de la variable 'url'.
            :return: None
        '''
        self._url = url

    @property
    def data(self):
        '''
        Getter de la variable 'data'.
        :return: La variable 'ur;'
        '''
        return self._data

    @data.setter
    def data(self, data):
        '''
            Setter de la variable 'data'.
            :return: None
        '''
        self._data = data

    def get(self):
        '''
        Función que devuelve la lista de arcos del árbol (si la hay) al hacer
        una petición GET al endpoint '/graph'.
        :return: Un JSON con los arcos del grafo.
        '''

        return {"data": "Graph API working..."}

    def put(self):
        '''
        Función encargada de recibir los datos necesarios para crear un grafo.
        Los recibe en formato JSON cuando se hace una petición PUT al endpoint.
        :return: Una tupla de la forma (num_personas_necesarias, [lista_de_personas_necesarias])
        '''
        # Verificamos que cumpla con los datos que necesitamos
        args = graph_put_args.parse_args()

        # Función encargada de tratar la entrada
        self.clean_data(args)

        # Iniciamos el grafo
        self.start_graph()

        # Le damos formato al JSON de respuesta
        self.data = {
            "distance": self.data[0],
            "nodes": self.data[1]
        }

        return self.data, 201

    def clean_data(self, args):
        # Guardamos el inicio y el objetivo
        self.start = args['start']
        self.goal = args['goal']

        # Separamos los arcos por parejas
        edges = args['edges'].split(',')

        # Separamos cada pareja
        edges = [tuple(map(int, edge.split('-'))) for edge in edges]

        # Guardamos los arcos en su variable respectiva
        self.arcs = edges

        # Modificamos la variable global
        for el in self.arcs:
            temp_graph.append(el)

    def delete(self):
        temp_graph.clear()
        return {"message": "Arcos borrados satisfactoriamente"}

    def are_arcs_empty(self):
        if len(temp_graph) == 0:
            abort(404, message="No se puede consultar un grafo sin nodos")

    def start_graph(self):
        self.g_instance = Graph(self.goal + 1)

        # Agregamos los arcos al grafo
        for pair in self.arcs:
            self.g_instance.add_edge(pair[0], pair[1])

        # Buscamos la cantidad de personas necesarias para llegar de 'start' a 'goal'
        self.data = self.g_instance.find_love(self.start, self.goal)
