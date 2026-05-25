#This is a Student Mark Manager

print("\n------STUDENT MARK MANAGER------")

student = {}

#using while loop 

while True:
    print("1. Add student")
    print("2. View All Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Select choice:")

    if choice == "1":
        name = input("Enter Student Name:")
        marks = int(input("Enter Student Marks:"))
        student[name] = marks
        print(name ,"Successfully Added")

    #ADD Student

    elif choice == "2":
        if not student:
            print("Data not found!")
        else:
            for name,marks in student.items():
                print(name,":",marks)

    #View All Student

    elif choice =="3":
        name = input("Enter Student name:")

        if name in student:
            marks = student[name]
            if marks >= 40:

                print("PASS")
            else:
                print("FAIL")
        else:
            print("Student not found!")
    

    #Exit 

    elif choice == "4":
        print("Exiting.....")
        break




    else:
        print("Invalid Input!")