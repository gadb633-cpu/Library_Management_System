from library_manager.validates import is_in_range_1_to_8,is_positive_num,is_not_empty
def get_num(msg):
    while True:
        try:
            num = int(input(f"{msg}:").strip())
            if is_positive_num and is_not_empty(num):
                return num
        except ValueError:
            print("Enter only a number,try again!")
def get_name(msg):
    while True:
        try:
            name = input(f"{msg}:").strip()
            if is_not_empty(name):
                return name
        except ValueError:
            print("please enter name,try again!")
