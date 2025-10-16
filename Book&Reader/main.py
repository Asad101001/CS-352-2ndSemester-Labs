from Reader import *
from Book import Book

#PART A
novel = Book("Python Tales", ["Introduction","Lists","Loops"])

r1 = novel.new_reader("Asad")
r2 = novel.new_reader("Rizzler")


next(r1)
next(r1)
next(r2)

novel = Book("Python Tales", ["Introduction","Lists","Loops"])

Asad = novel.new_reader("Asad")
Rizzler = novel.new_reader("Rizwan")

for i,page in enumerate(Asad):
    if i == 1:
        novel._pages.append("Functions")

print("\n Now Ayesha starts:\n")

for page in Rizzler:
    pass
