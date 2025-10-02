def check_branch(value):
    while True:
        branch = input(value)
        if branch.title() in valid_branches:
            return branch.title()
        else:
            print(f"Invalid branch! Choose from {valid_branches}")

def check_admission_year(value):
    while True:
        try:
            admission_year = int(input(value))
            if admission_year > 0:
                return admission_year
            else:
                print("Admission year must be positive!")
        except ValueError:
            print("Please enter a valid number!")

def check_phone(value):
    while True:
        phone = input(value)
        if phone.isdigit() and len(phone) == 10:
            return phone
        else:
            print("Please enter a valid 10-digit phone number!")

def check_email(value):
    while True:
        email = input(value)
        if "@" in email and "." in email and not email[0].isdigit():
            return email
        else:
            print("Please enter a valid email address!")

def check_cgpa(value):
    while True:
        try:
            cgpa = float(input(value))
            if 0 <= cgpa <= 10:
                return cgpa
            else:
                print("CGPA must be between 0 and 10.")
        except ValueError:
            print("Please enter a valid CGPA!")

def check_year(value,admission_year):
    while True:
        try:
            year = int(input(value))
            if year >= admission_year:
                return year
            else:
                print("Previous academic year should be greater or equal to Admission Year.")
                continue
        except ValueError:
            print("Please enter a valid year!")

def add_student():
    while True:
        roll_no = input("Enter the Roll No. : ")
        if roll_no not in students:
            name = input("Enter the Name : ")
            branch = check_branch("Enter Branch : ")
            admission_year = check_admission_year("Enter Admission Year : ")
            phone = check_phone("Enter Phone Number : ")   
            email = check_email("Enter E-mail : ")
            contact = (phone,email)
            semester = input("Enter the last semester : ")
            cgpa = check_cgpa("Enter cgpa : ")
            year = check_year("Enter Previous academic year : ",admission_year)
            history = (semester,cgpa,year)
            value = {"name" : name.title(), "branch" : branch, "admission_year" : admission_year, "contact" : contact, "academic_history" : history}
            students[roll_no] = value
            print("Details Added Successfully")
        else:
            print("The Roll No. already exists.")
        more = input("Enter 'Y' to add more student or any other key to EXIT : ")
        if more in ['y','Y']:
            continue
        else:
            break

def fetch_student():
    while True:
        roll_no = input("Enter the Roll No. : ")
        if roll_no in students:
            data = students[roll_no]
            print(f"Name: {data['name']}")
            print(f"Branch: {data['branch']}")
            print(f"Admission Year: {data['admission_year']}")
            print(f"Contact: Phone- {data['contact'][0]}, Email- {data['contact'][1]}")
            print(f"Academic History: Semester- {data['academic_history'][0]}, CGPA- {data['academic_history'][1]}, Year- {data['academic_history'][2]}")
            seniority = 2025 - data["admission_year"]
            print(f"Seniority: {seniority} years")
        else:
            print("Student not found")
        more = input("Enter 'Y' for fetching more student details or any other key to EXIT : ")
        if more in ['y','Y']:
            continue
        else:
            break

def update_student():
    roll_no = input("Enter the Roll No. : ")
    if roll_no in students:
        while True:
            print("===== What you want to update ? =====")
            print("1. Enter 1 for updating Name")
            print("2. Enter 2 for updating Branch")
            print("3. Enter 3 for updating Admission Year")
            print("4. Enter 4 for updating Contact Details")
            print("5. Enter 5 for updating Academic History")
            print("6. Enter any other key to EXIT")
            choice = input("Enter your choice : ")
            data = students[roll_no]
            match choice:

                case '1':
                    old_name = data["name"]
                    newname = input("Enter new Name : ").title()
                    data["name"] = newname
                    print(f"Name updated from {old_name} to {newname}")

                case '2':
                    old_branch = data["branch"]
                    newbranch = check_branch("Enter new Branch : ")
                    data["branch"] = newbranch
                    print(f"Branch updated from {old_branch} to {newbranch}")

                case '3':
                    old_admission_year = data["admission_year"]
                    new_admission_year = check_admission_year("Enter new Admission Year : ")
                    data["admission_year"] = new_admission_year
                    print(f"Admission Year updated from {old_admission_year} to {new_admission_year}")

                case '4':
                    old_contact = data["contact"]
                    new_phone = check_phone("Enter Phone number : ")
                    new_email = check_email("Enter new email : ")
                    new_contact = (new_phone,new_email)
                    data["contact"] = new_contact
                    print(f"Contact updated from {old_contact} to {new_contact}")

                case '5':
                    admission_year = data["admission_year"]
                    old_history = data["academic_history"]
                    semester = input("Enter new last semester : ")
                    new_cgpa = check_cgpa("Enter new cgpa : ")
                    new_year = check_year("Enter new Previous academic year : ",admission_year)
                    new_history = (semester,new_cgpa,new_year)
                    data["academic_history"] = new_history
                    print(f"History updated from {old_history} to {new_history}")

                case _:
                    print("Exiting from Updating Details")
                    break

            check = input("Enter 'Y' for Updating more details or any other key to EXIT : ")
            if check in ['y','Y']:
                continue
            else:
                print("Exiting form Updating Details")
                break
    else:
        print("Student not found")

def display_all():
    if not students:
        print("No student records available.")
        return
    print(f"{'Roll No':<10} | {'Name':<15} | {'Branch':<20} | {'CGPA'}")
    for i, data in students.items():
        history = data["academic_history"]
        cgpa = history[1]
        print(f"{i:<10} | {data['name']:<15} | {data['branch']:<20} | {cgpa:.2f}")

def find_by_branch():
    branch = check_branch("Enter the Branch : ")
    found = False
    for i in students:
        if branch == students[i]["branch"]:
            print(f"{i} | {students[i]['name']}")
            found = True
    if not found:
        print("No students found in this branch.")

def compare_cgpa():
    roll_no_1 = input("Enter 1st Roll No. : ")
    roll_no_2 = input("Enter 2nd Roll No. : ")
    if roll_no_1 not in students or roll_no_2 not in students:
        print("One or both roll numbers not found.")
        return
    elif roll_no_1==roll_no_2:
        print("You are comparing to the student itself.")
        return
    data1 = students[roll_no_1]
    academic_history1 = data1["academic_history"]
    cgpa1 = academic_history1[1]
    data2 = students[roll_no_2]
    academic_history2 = data2["academic_history"]
    cgpa2 = academic_history2[1]
    if cgpa1 > cgpa2:
        print(f"Roll No. {roll_no_1} has Higher cgpa")
    elif cgpa1 < cgpa2:
        print(f"Roll No. {roll_no_2} has Higher cgpa")
    else:
        print("Both have equal cgpa")

students = { }
valid_branches = ["Computer Science", "Electronics", "Mechanical", "Civil"]
while True:
    print("===== Student Information Management System =====")
    print("1. Enter 1 to Add a new student: ")
    print("2. Enter 2 to Fetch and display student info: ")
    print("3. Enter 3 to Update student details: ")
    print("4. Enter 4 to Display all students: ")
    print("5. Enter 5 to Find students by branch: ")
    print("6. Enter 6 to Compare academic performance: ")
    print("7. Enter any other key to Exit: ")
    choice = input("Enter your choice : ")
    match choice:
        case '1': add_student()
        case '2': fetch_student()
        case '3': update_student()
        case '4': display_all()
        case '5': find_by_branch()
        case '6': compare_cgpa()
        case _ :
            print("Exiting.....")
            break
