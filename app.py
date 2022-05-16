from flask import Flask #spark
from flask_restful import Api, Resource, reqparse #api restful
from flask_cors import CORS #CORS

import sys
sys.path.append(".") #necesito archivos de otras carpetas

# Importamos los archivos que necesitamos
from FileAnalyzer.file_analyzer_api import FileAnalyzerApi

# Creamos la aplicación
app = Flask(__name__)
CORS(app)
api = Api(app)

# Generamos el endpoint para la funcionalidad del algoritmo de Djikstra
api.add_resource(FileAnalyzerApi, "/api/v1/file")