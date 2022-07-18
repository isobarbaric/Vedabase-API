
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
        for file in sorted(os.listdir('json/gita')):
            with open('json/gita/' + file, 'r') as storage:
                self.chapters.append(json.load(storage))

# a = BhagavadGita()
# print(len(a.chapters))
# print(a.epilogue)

