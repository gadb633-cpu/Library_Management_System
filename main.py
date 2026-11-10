from db.list_books import get_list_of_books
from library_manager.result import shaw_menu
def main():
    status_loop = True
    books = get_list_of_books()
    while status_loop:
        menu = shaw_menu()
        

if __name__ =="__main__":
    main()    