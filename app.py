from src.config import *
from flask import *
from flask_restx import Api, Resource
from src.rcmd.rcmdController import namespace as rcmdNamespace

app = Flask(__name__)
api = Api(app)

api.add_namespace(rcmdNamespace, path='/api/rcmd')

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)