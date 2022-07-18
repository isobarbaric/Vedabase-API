
from flask import Flask
from flask_restful import Api, Resource

from gita import BhagavadGita

gita = BhagavadGita()

app = Flask(__name__)
api = Api(app)

class addendum(Resource):
    def get(self, addendum_type):
        if addendum_type in gita.preamble:
            return gita.preamble[addendum_type], 200
        print(gita.epilogue)
        if addendum_type in gita.epilogue:
            return gita.epilogue[addendum_type], 200
        return {'message': 'The addendum type provided is invalid.'}, 400
api.add_resource(addendum, '/gita/<string:addendum_type>/')

class chapter(Resource):
    def get(self, chapter_number):
        if chapter_number < 1 or chapter_number > 18:
            return {'message': 'The chapter number provided is invalid.'}, 400
        return gita.chapters[chapter_number-1], 200
api.add_resource(chapter, '/gita/<int:chapter_number>/')

class verse(Resource):
    def get(self, chapter_number, verse_number):
        if chapter_number < 1 or chapter_number > 18:
            return {'message': 'The chapter number provided is invalid.'}, 400
        if str(verse_number) not in gita.chapters[chapter_number-1]['verses']:
            return {'message': 'The verse number provided is invalid.'}, 400
        return gita.chapters[chapter_number-1]['verses'][str(verse_number)], 200
api.add_resource(verse, '/gita/<int:chapter_number>/<int:verse_number>/')

if __name__ == "__main__":
    app.run(debug=True)
