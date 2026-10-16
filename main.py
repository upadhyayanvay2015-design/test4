class Book:
    def __init__(self, title, author, is_borrowed=False):
        print("What book do you want to borrow?: ")
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def borrow_book(self):
        self.is_borrowed = True
    def return_book(self):
        self.is_borrowed = False
    def display_info(self):
        if self.is_borrowed:
            print(f"The book '{self.title}' by {self.author} is currently borrowed.")
        else:
            print(f"The book '{self.title}' by {self.author} is available.")

        if self.is_borrowed:
            print(f"The book '{self.title}' by {self.author} has been borrowed.")
        else:
            print(f"The book '{self.title}' by {self.author} is available.")