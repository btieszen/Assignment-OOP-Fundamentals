#Task 1: Vehicle Registration System
#- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner.
# Implement a method update_owner to change the vehicle's owner.
# Then, create a few instances of Vehicle and demonstrate changing the owner.




class Vehicle:
    def __init__(self,reg_num,type,owner):
        self.registration_number=reg_num
        self.type=type
        self.owner=owner
        
    def update_owner(self,new_owner):
        self.owner = new_owner
        
    def display_details(self):
        print(f"Owner: {self.owner}, Registration: {self.registration_number}, Type: {self.type}")
        
vehicles={}
    
def register_vehicles(reg_num,type,owner):
    if  reg_num in vehicles:
        print("Sorry registration already exist""\n")
        return
    vehicles[reg_num] = Vehicle(reg_num,type,owner)
    print(" Vehicle", {reg_num}, "has been registered""\n")
            
def update_vehicle_owner(number_update,new_owner):
    if number_update in vehicles:
        vehicles[number_update].update_owner(new_owner)
        print(f" Vehicle {number_update} has been updated""\n")
    else: 
        print("Vehicle not found""\n")
            
def display_all_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_details()
            
while True:
    def main():
        print("")
        print('Welcome to the DMV Registration')
        print('What would you like to do today:')
        print('1: Register a vehicle')
        print('2: Update a registration')
        print('3: Display all registered vehicles')        
        print('4: Exit''\n')
        choice=input("Please make your selection 1-4: ")
  
        if choice=="1":
            reg_num=input("Enter the registration number: ")
            type=input("What type of vehicle is it: ")
            owner=input("What is the name of the owner: ")
            register_vehicles(reg_num,type,owner)
        elif choice=="2":
            number_update=input("Enter the vehicle registration number: ")
            new_owner = input("Enter the new owner's name: ")
            update_vehicle_owner(number_update,new_owner)
        elif choice =="3":
            display_all_vehicles()
        elif choice=="4":
            print("Thank you for visiting the DMV""\n")
            
        else:
            print("Invalid choice please try again""\n")
    main()
                
    