
from flask import Flask
from flask_restful import Api, Resource

from gita import BhagavadGita

app = Flask(__name__)
api = Api(app)

gita = BhagavadGita()

class bGita(Resource):
    def get(self, chapter_number):
        return gita.chapters[chapter_number-1]

api.add_resource(bGita, '/gita/<int:chapter_number>/')

if __name__ == "__main__":
    app.run(debug=True)


