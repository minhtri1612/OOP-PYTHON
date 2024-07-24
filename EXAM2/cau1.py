class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(f"Book Name: {self.name}, Price: ${self.price:.2f}")

class CD:
    def __init__(self, cd_id, price):
        self.cd_id = cd_id
        self.price = price

    def describe(self):
        print(f"CD ID: {self.cd_id}, Price: ${self.price:.2f}")


class Library:
    def __init__(self, name):
        self.name = name
        self.list = []

    def add_media(self, media):
        self.list.append(media)

    def describe(self):
        print(f"Library Name: {self.name}")
        print("Media in the Library:")
        for item in self.list:
            item.describe()

library = Library("City Library")
book1 = Book("The Great Gatsby", 10.99)
book2 = Book("1984", 8.99)
library.add_media(book1)
library.add_media(book2)
cd1 = CD("CD12345", 14.99)
library.add_media(cd1)
library.describe()
