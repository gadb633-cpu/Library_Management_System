from db.list_books import BOOKS
from library_manager.result import shaw_menu,display_books
from library_manager.inputs import get_num,get_name
from library_manager.validates import is_positive_num,is_in_range_0_to_8
from library_manager.crud_books import add_book,borrow_book,search_book,get_next_book_id
def main():
    status_loop = True
    while status_loop:
        menu = shaw_menu()
        choice_option = get_num("Choose an option(0-8)")
        if is_in_range_0_to_8(choice_option) == False:
            continue
        if choice_option ==1:
            display_books(BOOKS)
        elif choice_option ==2:
            print(search_book(BOOKS,get_name("enter name")))
        elif choice_option ==3:
            pass
        elif choice_option ==4:
            pass
        elif choice_option ==5:
            pass
        elif choice_option ==6:
            pass
        elif choice_option ==7:
            pass
        elif choice_option ==8:
            pass    
        elif choice_option ==0:
            status_loop = False


if __name__ =="__main__":
    main()    