
kmlist = [5, 10, 20, 30, 50, 60, 100]
kmconvert = list(map(lambda x: x/1.609, kmlist))
# print(kmconvert)

def login():

    employees = [
        (0, "Julian", "Kaipo282"), 
        (1, "Annika", "Kanyon282"), 
        (2, "Dale", "Fezzick808"), 
        (3, "Shawna", "Runner808")
    ]

    counter = 3

    while counter > 0:

        username_input = input("Please enter your username: ")

        employee_password = input("Please enter your password: ")

        employee_mapping = {employee[1]: employee for employee in employees}

        try:
            _, username, password = employee_mapping[username_input]
            if employee_password == password:
                print("Successful Login!")
                break

            else:
                counter -= 1 
                print("password or username incorrect.")
                print(f"{counter} tries left.")
                continue
    
        except KeyError:
            print("Username not in database")
            continue



login()