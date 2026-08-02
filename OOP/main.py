class Book:
  def __init__(self,title,copies,status):
    self.title = title
    self.copies = copies
    self.status = status

def library_analyzer(books_records):
  valid_books = 0
  invalid_books = 0
  available_books = 0
  low_stock = 0
  out_stock = 0
  stocked_book = 0

  Book_objects = []

  for record in books_records:
    if record == "END":
      break
    if record == "":
      continue
    parts = record.split()

    if len(parts) != 2:
        invalid_books += 1
        continue

    title = parts[0]
    copies = parts[1]

    if not copies.isdigit():
        invalid_books += 1
        continue

    copies = int(copies)
    if copies < 0:
       invalid_books += 1
       continue

    valid_books += 1

    if copies == 0:
       status = "Out of stock"
       out_stock += 1
    elif copies <= 3:
       status = "Low Stock"
       low_stock += 1
    elif copies <= 10:
       status = "Stock Avaible"
       available_books += 1
    else:
       status = "Well Stocked"
       stocked_book += 1

    book_obj = Book(title,copies,status)
    Book_objects.append(book_obj)
    print(f"\nLetters in {title}:")
    for letter in title:
       print(letter)
  return (
     Book_objects,
     valid_books,
     invalid_books,
     available_books,
     low_stock,
     out_stock,
     stocked_book
    )
records = []
num = int(input("how many book records do you want to enter ? "))
for i in range(num):
   record = input(f"Enter record {i+1}(Title copies): ")
   records.append(record)

result = library_analyzer(records)
books = result[0]

print("\n========== LIBRARY REPORT ==========")

print(f"Valid Books      : {result[1]}")
print(f"Invalid Books    : {result[2]}")
print(f"Available Books  : {result[3]}")
print(f"Low Stock Books  : {result[4]}")
print(f"Out of Stock     : {result[5]}")
print(f"Well Stocked     : {result[6]}")

print("\nBook Details")

for book in books:
    print(f"{book.title} | Copies: {book.copies} | Status: {book.status}")
