class book:
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










