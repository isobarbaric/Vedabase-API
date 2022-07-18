
from addendum_finder import PreambleFinder, EpilogueFinder
from chapter_finder import ChapterFinder

import os
import json

class BhagavadGita:

    def __init__(self):
        # didn't bother putting preamble in json since its so short anyway
        self.preamble = PreambleFinder().find()
        self.chapters = []
        self.epilogue = EpilogueFinder().find()

        # self.content = ChapterFinder().find()
        files = sorted(os.listdir('json/gita'), key = lambda x: int(x[x.rfind('_')+1:x.rfind('.')]))
        for file in files:
            with open('json/gita/' + file, 'r') as storage:
                self.chapters.append(json.load(storage))

# a = BhagavadGita()
# print(len(a.chapters))
# print(a.epilogue)

