from library_manager.validates import is_in_range_0_to_8,is_positive_num
def get_num(msg):
    while True:
        try:
            num = int(input(f"{msg}:"))
            if is_positive_num:
                return num
        except ValueError:
            print("Enter only a number,try again!")
