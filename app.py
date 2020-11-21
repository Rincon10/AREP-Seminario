from flask import Flask
from flask_restful import Api, Resource, reqparse

import sys
sys.path.append(".")

# Importamos los archivos que necesitamos
from Graph.graph_api import GraphApi
from PriorityQueue.priority_queue_api import PriorityQueueApi
from DisjointSets.disjoint_sets_api import DisjointSetsApi

# Creamos la aplicación
app = Flask(__name__)
api = Api(app)


# Generamos el endpoint para la funcionalidad de grafos
api.add_resource(GraphApi, "/graph")

# Generamos el endpoint para la funcionalidad de cola de prioridad
api.add_resource(PriorityQueueApi, "/priority_queue")

# Generamos el endpoint para la funcionalidad de cola de prioridad
api.add_resource(DisjointSetsApi, "/sets")
