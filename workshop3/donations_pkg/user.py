def login(database, username, password):
    if username in database and database[username] == password:
        print("\nWelcome back", username + "!")
        return username
        
    elif username in database[username] != password:
        print("\nIncorrect password for", username + ".")
        return ""
    else:
        print("\nUser not found. Please register.")
        return ""


def register(database, username):
    if username in database:
        print("\n you are already registerd", {username} + "!")
        return ""
