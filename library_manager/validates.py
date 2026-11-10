
def is_positive_num(num):
    if num > 0:
        return True
    return False

def is_in_range_1_to_8(num):
    if num <= 0 or num >8:
        print("only between 1-8!")
        return False
    return True
def is_book_already_borrow(book, book_id):
    if book["id"] == book_id:
        return book["available"]
def is_not_empty(item):
    if item == "":
         return False
    return True        
def if_book_id_exist(book,book_id):
    if book["id"] == book_id:
        return True
    return False    
def if_author_exist(book,book_id):
    if book["id"] == book_id:
        return True
    return False  
     