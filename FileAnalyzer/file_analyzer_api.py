from flask_restful import Resource, reqparse, abort
import sys
sys.path.append(".")
from FileAnalyzer.file_analyzer import FileAnalyzer

graph_put_args = reqparse.RequestParser()
graph_put_args.add_argument("url", type=str, help="URL is required", required=True)

class FileAnalyzerApi(Resource):
    def __init__(self):
        # URL
        self._url = None

        # File Analyzer instance
        self._f_instance = None

        # Response
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
    def f_instance(self):
        '''
        Getter de la variable 'f_instance'.
        :return: La variable 'ur;'
        '''
        return self._f_instance

    @f_instance.setter
    def f_instance(self, f_instance):
        '''
            Setter de la variable 'f_instance'.
            :return: None
        '''
        self._f_instance = f_instance

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

        return {"data": "File Analyzer API working..."}

    def put(self):
        # Verificamos que cumpla con los datos que necesitamos
        args = graph_put_args.parse_args()

        # Función encargada de tratar la entrada
        self.clean_data(args)

        # We call the file analyzer logiv
        self.start()

        return self.data, 201

    def clean_data(self, args):
        # We save the URL
        self.url = args["url"]

        self.f_instance = None

    def start(self):
        # We create an instance of the FileAnalyzer object
        self.f_instance = FileAnalyzer(self.url)

        # We create the object response 
        self.data = self.f_instance.createInformation()    
