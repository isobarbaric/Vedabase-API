
class Chapter:

    def __init__(self, chapterNumber: int, chapterTitle: str, verses: list):
        self.chapterNumber = chapterNumber
        self.chapterTitle = chapterTitle
    

class BhagavadGita:
    
    def __init__(self):


# # Bhagavad-gītā As It Is

# - deal with these parts of the book individually
#     - Setting the Scene
#     - Dedication
#     - Preface
#     - Introduction
#     - A Note About the Second Edition
# - for the ``Chapter``s:
#     - variables
#         - chapter number
#         - chapter title
#         - list of ``Text`` objects
#     - API methods unique to ``Chapter`` objects are getters for the first 2 variables mentioned
# - for the ``Text``s:

#         - text number
#         - text devanagri
#         - text romanization
#         - synonyms
#         - translation
#         - purport
#     - API methods unique to ``Text`` objects are getters for the variables mentioned above

# for the API itself, have to figure out the routes for the calls themselves individually later and there, can combine calls to these functions
