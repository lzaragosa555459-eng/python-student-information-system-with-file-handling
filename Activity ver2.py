import os 
idList = []
nameList = []
ageList = []
gradeList = []
#This four list are created as a storage for the values

file_name = "Student.txt"

list_names = ["list1","list2","list3","list4"]
MasterLIST = {"list1":idList,"list2":nameList,"list3":ageList,"list4":gradeList}
# MasterList in dictionary


#lines 15 to 112 are fuctions
def add_student():
    print("<ADD>==========================================")
    print("Note* please carefully input the data.")
    ID = input("<ID> ")
    Name = input("<Name> ")
    Age = input("<Age> ")
    Grade = input("<Grade> ")

    idList.append(ID)
    nameList.append(Name)
    ageList.append(Age)
    gradeList.append(Grade)
    print("Data added successfully!*")
    print("===============================================")

def update_student():
    if len(idList) > 0:
                print("<UPDATE>=======================================")
                print("--Note: the index starts with 0 until 3. choose between these numbers--")
                try:
                    get_number = int(input("<[0]ID [1]NAME [2]AGE [3]GRADE> "))
                    selected_list_name = list_names[get_number]
                    selected_list = MasterLIST[selected_list_name]
                    print("Index\tLists")
                    for x in range(len(idList)):
                        print(f"{x}\t{selected_list[x]}")

                    print("--Note: the index starts with 0 until",len(idList)-1,". choose between these numbers--")
                    get_number = int(input("<WHICH_INDEX> "))
                    try:
                        update_value_index = input("<UPDATE_VALUE> ")
                        selected_list[get_number] = update_value_index
                        print("Data Updated successfully!*")
                    except:
                        print("Error: The index is overbound and cannot be",get_number)
                except:
                    print("Error: The index is overbound and cannot be",get_number)
                print("===============================================")
    else:
        print("Error: You cannot update anything with no data added or the records are empty.*")

def delete_student():
    if len(idList) > 0:
                print("<DELETE>=======================================")
                try:
                    print("--Note: the index starts with 0 until",len(idList)-1,". choose between these numbers--")
                    get_number = int(input("<ENTER_ID> "))
                    del idList[get_number]
                    del nameList[get_number]
                    del ageList[get_number]
                    del gradeList[get_number]
                    print("Record deleted successfully!*")
                except:
                    print("There is nothing to delete.*")
                print("===============================================")
    else:
        print("Error: You cannot delete anything with no data added or the records are empty.*") 

def display_student():
    if idList and nameList and  ageList and gradeList is not None:
                print("<DISPLAY>=========================================")
                print("ID\tNAME\t\tAGE\tGRADE\t")
                for id, name, age, grade in zip(idList, nameList, ageList, gradeList):
                    print(f"{id}\t{name}\t{age}\t{grade}")
                print("===============================================")
    else:
        print("Error: You cannot Display anything with no data added or the records are empty.*")

def save_to_file():
    if len(idList) > 0:
                print("<SAVE--TO--FILE>===============================")
                try:
                    with open(file_name,"a") as file:
                        for id, name, age, grade in zip(idList, nameList, ageList, gradeList):
                            file.write("{:<3}\t{:<20}\t{:<3}\t{:<3}\n".format(id[:],name[:],age[:],grade[:]))
                            print("--Data successfully saved!--")
                except FileNotFoundError:
                    print("--Error: file cannot be saved--")
                print("===============================================")
    else:
        print("Error: You cannot save anything with no data added or the records are empty.*") 

def load_from_file():
    if os.path.getsize(file_name) != 0:
                try:
                    with open(file_name,"r") as file:
                        ReadFile = file.read()
                        if ReadFile is not None:
                            print("<LOAD--FROM--FILE>=============================")
                            print("-----------------------------------------------")
                            print("ID\tNAME\t\t\tAGE\tGRADE\t")
                            print(ReadFile)
                            print("-----------------------------------------------")
                            print("===============================================")
                        else:
                            print("The values are empty...")
                except FileNotFoundError:
                    print("--Error: file cannot be loaded.--")
    else: 
        print("Error: the file is empty or you haven't saved a record.*")


#Use while loop True
while True:
    Choice = int(input("""===== Student Information System =====
1. Add Student
2. Display Student
3. Update Student
4. Delete Student
5. Save to File
6. Load from File
7. Exit\nEnter your choice>> """))
    
#This is match case where we call the functions
    match Choice:
        case 1:
           add_student()
        case 2:
            display_student()
        case 3:
            update_student()
        case 4:
            delete_student()
        case 5:
            save_to_file()
        case 6:
            load_from_file()
        case 7:
            print("--Exit-- ",end="")
            print("B-)")
            break
        case _: 
            print("Error: Invalid input. Try again.*")