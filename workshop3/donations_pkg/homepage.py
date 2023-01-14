def show_homepage():      # Main menu to choose options
    print("     ===    DonateMe Homepage   ===")
    print("----------------------------------------")
    print("| 1.   Login   | 2.   Register          |")
    print("----------------------------------------")
    print("| 3.   Donate  | 4.   Show Donations    |")
    print("----------------------------------------")
    print("|            5.  Exit                   |")
    print("----------------------------------------")


def donate(username):  # allows user to insert the donation amount.
    donation_atm = float(input("Enter amount to donate: "))
    donation_string = username + "donated $" + str(donation_atm)
    print("\nthank you for the donation!")
    return donation_string  # return the deposit amount with username.


def show_donations(donations):  # Display donation history.
    print("\n--- All Donations ---")
    if donations == []:
        print("currently there are no donations")
    else:
        for item in donations:  # listing donations that have been submited.
            print(item)
