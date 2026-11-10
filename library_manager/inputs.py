
def get_num(msg):
    try:
        num = int(input(f"{msg}:"))
        return num
    except ValueError:
        print("Enter only a number,try again!")
        