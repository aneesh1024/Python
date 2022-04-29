print("\t\t ---------------------------")
print("\t\t |Student Management System|")
print("\t\t ---------------------------")
exit = "no"
stud_list = []
while exit.lower() == "no" or exit.lower() == 'n':
    choice = int(input("Press 1 for adding Students or 2 for viewing students : "))
    if choice == 1:
        while choice == 1:
            num_stud = int(input("How many students do you want to add : "))
            for i in range(0,num_stud):
                print(f"\nEnter details of student {i+1}")
                stud_info = {'Name':'','Age':'','Course':'','Branch':''}
                stud_info['Name'] = input("Enter the studnet's name : ")
                stud_info['Age'] = input("Enter the studnet's age : ")
                stud_info['Course'] = input("Enter the course enrolled by the student : ")
                stud_info['Branch'] = input("Enter the branch : ")
                stud_list.append(stud_info)
            choice = int(input("Enter 1 to add more stduents or 2 to print informations of the students : "))    
    if choice == 2:
        if len(stud_list) == 0:
            print("There are no students entered in the list")
        else:
            for i in  stud_list:
                print(f"\n({stud_list.index(i)+1}.)",end = " ")
                for a,b in i.items():
                    print(f"{a} : {b}")
    exit = input("Exit ? : ")
    