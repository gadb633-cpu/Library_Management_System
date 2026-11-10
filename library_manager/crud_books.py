from db.list_books import BOOKS
from library_manager.validates import is_book_already_borrow,if_book_id_exist,if_author_exist,if_name_exist

def search_book(books, name):
    new_books = []
    for book in books:
        if name.lower() in book["name"].lower():
            new_books.append(book)
            continue
    if new_books ==[]:
        return "not found"    
    return new_books    
def get_next_book_id(books):
    return len(books)+1

def add_book(books, name, author, year):
    for book in books:
        if if_name_exist(book,name) and if_author_exist(book,author):
            return "it's already exists"
    book_id = get_next_book_id(books)
    new_book = {"id": book_id,"name": name,"author": author,"year": year,"available": True}
    books.append(new_book)
    return True

def borrow_book(books, book_id):
    for book in books:
        if is_book_already_borrow(book,book_id) and if_book_id_exist(book,book_id):
            if book["id"] == book_id:
                book["available"] = False
                return "ok"
    return "not found"            

def return_book(books, book_id):
    for book in books:
        if is_book_already_borrow(book,book_id) == False:
            if book["id"] == book_id:
                book["available"] = True
                return "ok"
    return "It already exists!"

def get_available_books(books):
    new_books = []
    for book in books:
        if book["available"] == True:
            new_books.append(book)
    return new_books 

def get_books_by_author(books, author):
    for book in books:
        if book["author"] == author:
            return book
    return "not found"          