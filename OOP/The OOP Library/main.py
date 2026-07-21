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
      print(f"Title : {current_book.title} | Author {current_book.author} | Status: {status}  ")

  def borrow_book(self,target_title):
    for book in self.bookshelves:
      if book.title == target_title:
        if book.is_available == True:
          book.is_available = False
          print(f"Enjoy reading! you have successfuly checked out '{book.title}")
          return
      else:
        print(f"Sorry, '{book.title}' is already learned out to someone else")
        return

    print(f"Error: '{target_title}' is not carried in our library system. ")


  def return_book(self, target_title):
        for book in self.bookshelves:
            if book.title == target_title:
                if book.is_available == False:
                    # Reset the toggle status to True so others can read it
                    book.is_available = True
                    print(f"🔄 Thank you! '{book.title}' is back on the shelf.")
                    return
                else:
                    print(f"Wait... '{book.title}' is already on our shelf. Are you sure?")
                    return
        print(f"❌ Error: '{target_title}' does not belong to this library branch.")
central_library = Library()
central_library.add_book(Book("The Hobbit", "J.R.R. Tolkien"))
central_library.add_book(Book("1984", "George Orwell"))
while True:
    print("\n==============================")
    print("   CITY LIBRARY MAIN MENU     ")
    print("==============================")
    print("1. View Catalogue")
    print("2. Donate / Add a New Book")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Exit System")
    user_choice = input("Select option (1-5)")
    if user_choice == "5":
      print("System shutting down.Have a wonderful day!")
      break
    elif user_choice == "1":
      central_library.display_books()
    elif user_choice == "2":
      book_name = input("Enter the book name : ")
      book_author = input("Enter book author : ")

      fresh_book_object = Book(title_input = book_name, author_input= book_author)
      central_library.add_book(fresh_book_object)
    elif user_choice == "3":
      title_to_find = input("enter the title of the book " )
      central_library.borrow_book(title_to_find)
    elif user_choice == "4":
      title_to_retrun = input("Enter the book name you want to return : ")
      central_library.return_book(title_to_retrun)
    else:
        print("Invalid choice configuration. Try selecting numbers between 1 and 5.")
