
def is_positive_num(num):
    if num > 0:
        return True
    return False

def is_in_range_0_to_8(num):
    if num < 0 or num >8:
        return False
    return True
def is_book_already_borrow(book, book_id):
        if book["id"] == book_id:
            return book["available"]
