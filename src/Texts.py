from src import words,mesage,date

class Texts():
    def __init__(self):
        self.words  = words
        self.mesage = mesage
        self.date   = date

    def getWords(self):
        return words

    def getMesage(self):
        return mesage

    def getDate(self):
        return date
