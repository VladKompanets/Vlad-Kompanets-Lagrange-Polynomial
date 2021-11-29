class HomeLibrary():

    def __init__(self,author, publication,genre):
        self.author = author
        self.publication = publication
        self.genre = genre
        print("Книга выбрана")


my_book = HomeLibrary("Dmitriy Portniagin",2018,"startup")
my_preferences = HomeLibrary("Ozan Varol",2020,"Business")
print(my_book.publication)
print(my_preferences.author)
print(my_preferences.genre)

