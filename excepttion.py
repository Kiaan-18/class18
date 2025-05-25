try:
    number=int(input("Enter any number:"))
    print("The entered number is",number)
except ValueError as ex:
    print("Exception happend ",ex)