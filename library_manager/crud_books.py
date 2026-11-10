from db.list_books import BOOKS
from library_manager.validates import is_book_already_borrow

def search_book(books, name):
    for book in books:
        if name in book["name"]:
            return book["name"]
    return None
def get_next_book_id(books):
    return len(books)+1

def add_book(books, name, author, year):
    book_id = get_next_book_id(books)
    book = {"id": book_id,"name": name,"author": author,"year": year,"available": True}
    books.append(book)
    return True

def borrow_book(books, book_id):
    for book in books:
        if is_book_already_borrow(book,book_id):
            if book["id"] == book_id:
                book["available"] = False
                