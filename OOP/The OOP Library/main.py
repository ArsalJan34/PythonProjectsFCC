class Book:
  def __init__(self, title_input, author_input):
    self.title = title_input
    self.author = author_input

    self.is_available = True

class Library:
  def __init__(self):
    self.bookshelves = []

  def add_book(self,book_obj):
    self.bookshelves.append(book_obj)
    print(f"Success: '{book_obj.title}' has been cataloged to the library.")
  def display_books(self):
    if len(self.bookshelves) == 0:
      print("The library currently has no books inside.")
      return
    print("\n ---Current Library Catalogue ---")
    for current_book in self.bookshelves:
      if current_book.is_available == True:
        status = "Available"
      else:
        status = "Checked Out"
