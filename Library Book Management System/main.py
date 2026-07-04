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
    record = record.split()

    if record != 2:




