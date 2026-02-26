class Book:
    def __init__(self, title, author, rating, price):
        self.title = title
        self.author = author
        self.rating = rating
        self.price = price

    def show_details(self):
        print(f"The title is {self.title}")
        print(f"The author is {self.author}")
        print(f"The rating is {self.rating}")
        print(f"The price is {self.price}")

class eBook(Book): # inheritance
    def __init__(self, title, author, rating, price, download_url):
        super().__init__(title, author, rating, price)
        self.download_url = download_url
    
    def show_details(self): #overriding (run time polymorphism)
        super().show_details()
        print(f"The download url is {self.download_url}")

eb1 = eBook("Learning Python", "Muhammad Ali", 8.4, 1100, "https://www.google.com/")
eb1.show_details()


