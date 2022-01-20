# author : Dhrumil Mevada
# importing the module
import sys


def load():
    l1 = []
    # open the file for reading
    with open("contacts.txt", "r") as fn:
        # for each line in the file
        for line in fn:
            l2 = []
            # read the line as a colon separated list
            line = line.split(':')
            # the name is the first list item
            # name = line[0]
            l2.append(line[0])
            # phone = []
            if len(line) == 2:
                l2.append(int(line[1]))
            elif len(line) == 3:
                l2.append(int(line[1]))
                l2.append(int(line[2]))
            elif len(line) == 4:
                l2.append(int(line[1]))
                l2.append(int(line[2]))
                l2.append(int(line[3]))
            elif len(line) == 5:
                l2.append(int(line[1]))
                l2.append(int(line[2]))
                l2.append(int(line[3]))
                l2.append(int(line[4]))
            elif len(line) == 6:
                l2.append(int(line[1]))
                l2.append(int(line[2]))
                l2.append(int(line[3]))
                l2.append(int(line[4]))
                l2.append(int(line[5]))
            l1.append(l2)

    return l1


def menu():
    # We created this menu function
    print("\n********************************************************************")
    print("\t\t\tPHONE DIRECTORY", flush=False)
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove a contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    choice = int(input("Please enter your choice: "))
    print("\n")
    return choice


# this function displays all content of phonebook pb
def display_all(pba):
    if not pba:
        # if display function is called after deleting all contacts then the len will be 0
        # And then without this condition it will throw an error
        print("Contacts is empty...")
    else:
        pba.sort()
        for i in range(len(pba)):
            print(pba[i])
    print("\n")


def add_contact(apb):
    # Adding a contact is the easiest because all you need to do is:
    # append another list of details into the already existing list
    enter = int(input("How Many contacts do you want to enter : "))
    # dip.clear()
    for i in range(0, enter):
        dip = []
        dip.append(str(input("Enter name: ")))
        # we assume that 1 person has maximum 5 contacts...
        enter_con = int(input("How many contacts numbers you want to add(maximum 5 contacts): "))
        for j in range(0, enter_con):
            num = input("Enter Contact number: ")
            dip.append(num)
        apb.append(dip)
    return apb


def delete_contact(bpb):
    # This function is to remove a contact's details from existing phonebook
    query = str(input("Please enter the name of the contact you wish to remove: "))

    temp = 0

    for i in range(len(bpb)):
        if query in bpb[i][0]:
            temp += 1
            print(bpb.pop(i))

            # printing a confirmation message after removal.
            print("Contact has now been removed\n")
            # This ensures that removal was successful.

            # After removal we will return the modified phonebook to the calling function
            return bpb

    if temp == 0:
        print("Sorry, you have entered an invalid query.\
    Please recheck and try again later.")

    return bpb


def delete_all(cpb):
    # This function will simply delete all the entries in the phonebook list

    # this File Handling code will delete all contacts from file...
    with open("contacts.txt", 'w') as f:
        pass

    # It will return an empty phonebook list after clearing
    return cpb.clear()


def search_contact(dpb):
    # This function searches for an existing contacts and displays the result

    temp = []
    check = -1
    query = str(input("Please enter the name/keyword of the contact you want to search: "))
    print("\n")
    for i in range(len(dpb)):
        if query in dpb[i][0]:
            check = i
            temp.append(dpb[i])

    if check == -1:
        print("The contact does not exist. Please try again\n")

    # all the searches are stored in temp and all the results will be displayed with
    # the help of display function
    else:
        display_all(temp)
    # return check


def thanks(rpb):
    if rpb != None:
        rpb.sort()

        with open("contacts.txt", 'w') as fn:
            for i in range(len(rpb)):
                for j in range(len(rpb[i]) - 1):
                    fn.write(str(rpb[i][j]))
                    fn.write(":")
                fn.write(str(rpb[i][len(rpb[i]) - 1]) + "\n")
    print("\n********************************************************************")
    print("Thank you for using our Phone Directory System...")
    sys.exit("Goodbye, have a nice day Ahead!!!\n")

# Main function code
print("\n====================================================================")
print("\tHello User, Welcome To Our Phone Directory System")
print("\tYou may now proceed to explore this directory")
print("====================================================================")

ch = 1
pb = load()  # load a contact in contact text file in pb list
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = delete_contact(pb)
    elif ch == 3:
        pb = delete_all(pb)
        # print(pb)
    elif ch == 4:
        search_contact(pb)
    elif ch == 5:
        display_all(pb)
    else:
        thanks(pb)