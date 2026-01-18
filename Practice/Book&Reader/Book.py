from Reader import Reader

class Book:

    def __init__(self, title, pages):
        self._title = title
        self._pages = pages

    
    def new_reader(self, name):
        return Reader(self._pages, name)