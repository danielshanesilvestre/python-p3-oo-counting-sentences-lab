#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) is str:
            self._value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        if (self.value[len(self.value) - 1] == "."):
            return True
        return False
        
    def is_question(self):
        if (self.value[len(self.value) - 1] == "?"):
            return True
        return False
        
    def is_exclamation(self):
        if (self.value[len(self.value) - 1] == "!"):
            return True
        return False

    def count_sentences(self):
        working = self.value

        working = working.replace("!", ".");
        working = working.replace("?", ".");
        unfiltered_sentences = working.split(".");
        sentences = [sentence for sentence in unfiltered_sentences if sentence != ""]

        return len(sentences)
