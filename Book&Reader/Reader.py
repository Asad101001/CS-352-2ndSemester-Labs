class Reader:

    def __init__(self, pages, name):
        self._pages = pages
        self._index = 0
        self._name = name

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= len(self._pages):
            raise StopIteration
        
        page = self._pages(self._index)
        print(f"{self._name} reads {page}")
        self._index += 1
        return page
        