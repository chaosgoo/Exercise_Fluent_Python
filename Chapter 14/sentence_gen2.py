import re
import reprlib

RE_WORD = "\w+"

class Sentence:

    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return "Sentence(%s)" % reprlib(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()