def num():
    while(True):
        num = input("Enter an integer: ")
        try:
            num = int(num)
            return num
        except:
            print("Wrong type of input. Please enter an integer ")