class Book:
    def __init__(self, title : str, author: str, year: int):
       self.title = title
       self.author = author
       self.year = year
       

b1 = Book("O‘tkan kunlar", "Abdulla Qodiriy", 1925)
b2 = Book("Mehrobdan chayon","Abdulla Qodiriy", 1929)
print(b1.title)
print(b2.title)
