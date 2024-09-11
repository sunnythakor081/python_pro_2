import python_M5 as Result


while True:
    print("1.Add Course")
    print("2.Drop Course")
    print("3.Print Course")
    print("4.Calculate CGPA")
    choice  = int(input("Enter Your Choice : "))

    if choice == 1:
        course = input("Enter your course : ")
        credit = int(input("Enter credit : "))
        earn = int(input("Enter earned credit : "))
        Result.add(course,credit,earn)

    if choice == 2:
        course = input("Enter course name to drop : ")
        Result.drop(course)

    if choice == 3: 
        Result.printList();

    if choice == 4:
        cgpa = Result.cgpa()
        print(f"CGPA : {cgpa}")

    if choice == 5:
        break

    


# Result.add("cs1100",10,8)
# Result.add("cs1200",10,9)
# Result.add("cs1300",20,18)
# Result.add("Activity",20,10)




# Result.printList()
# cgpa = Result.cgpa()
# print(f"CGPA : {cgpa}")