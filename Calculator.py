def check_value(value):
    while True:
        try:
            return float(input(value))
        except ValueError:
            print("Enter Valid Number...")

def addition():
    first_value = check_value("Enter the First Value : ")
    add = first_value
    while True:
        other_value = check_value("Enter the Other Value : ")
        add += other_value
        check = input("Enter 'Y' for adding More Values or any other key to EXIT : ")
        if check not in ['y','Y']:
            break
    print(f"Addition of Entered Values is : {add:.2f}\n")

def subtraction():
    first_value = check_value("Enter the First Value : ")
    sub = first_value
    while True:
        other_value = check_value("Enter the Other Value : ")
        sub -= other_value
        check = input("Enter 'Y' for subtracting More Values or any other key to EXIT : ")
        if check not in ['y','Y']:
            break
    print(f"Subtraction of Entered Values is : {sub:.2f}\n")

def multiplication():
    first_value = check_value("Enter the First Value : ")
    multiply = first_value
    while True:
        other_value = check_value("Enter the Other Value : ")
        multiply *= other_value
        check = input("Enter 'Y' for multiplying More Values or any other key to EXIT : ")
        if check not in ['y','Y']:
            break
    print(f"Multiplication of Entered Values is : {multiply:.2f}\n")

def division():
    first_value = check_value("Enter the First Value : ")
    divide = first_value
    while True:
        other_value = check_value("Enter the Other Value : ")
        if other_value == 0:
            print("Enter Apropriate Value...")
            continue
        divide //= other_value
        check = input("Enter 'Y' for division- More Values or any other key to EXIT : ")
        if check not in ['y','Y']:
            break
    print(f"Division of Entered Values is : {divide:.3f}\n")


while True:
    print("===== Calculator Menu =====")
    print("1. Press 1 for Addition")
    print("2. Press 2 for Subtraction")
    print("3. Press 3 for Multiplication")
    print("4. Press 4 for Division")
    print("5. Press any other key to EXIT")
    choice = input("Enter your choice : ")
    if choice in ['1', '2', '3', '4']:
        choice = int(choice)
    match choice:
        case 1: addition()
        case 2: subtraction()
        case 3: multiplication()
        case 4: division()
        case _: break
print("Thank you for using the Calculator. Good Byee...")
