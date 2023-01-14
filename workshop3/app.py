# login and register verifcation functions.
from donations_pkg.user import login, register
# importing  functions to make app run the options.
from donations_pkg.homepage import show_homepage, donate, show_donations


database = {"admin": "password123"}  # key username and password for login
donations = []
authorized_user = ""
while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print("Logged in as:", authorized_user)  # valid user succesfully login

    choice = input("Choose an option: ")  # select option off of the mainpaige.
    if choice == "1":
        username = input("enter Username")
        password = input("enter password")
        authorized_user = login(database, username, password)
    elif choice == "2":
        username = input("enter username")
        password = input("enter password")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password

    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif choice == "4":
        show_donations(donations)

    elif choice == "5":
        print("Good bye!")
        break
