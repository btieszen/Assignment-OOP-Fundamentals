

def update_participant(name):
    new_name= input("Enter name: ")
    if new_name in name:
        print("Guest already exists")
    else:
        name.append(new_name)
        print(f"Guest {new_name} has been added""\n")
        print(name)


        





