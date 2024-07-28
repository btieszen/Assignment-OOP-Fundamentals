#Task 2: Event Management System Enhancement
#roblem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
# Implement a method add_participant that increases the count 
# and a method get_participant_count to retrieve the current count.


import get_participant_count
import add_participant

class Event:
    def __init__(self, count,name):
        self.count = count
        self.name = name
        
    def participate_count(self):
        print(" The total guest count is" ,(get_participant_count.total_customer_count()))
        
    def update_guest(self,new_name):
        self.name =new_name
        #add_participant.update_participant(new_name)
        
    
        
    
name=["Brian","Sara"]  


def updated_list(new_name):
    add_participant.update_participant(new_name)

        


         
def main():
    while True:
        print("Welcome to your guest count for your event")
        print ("1: Total number of guest:")       
        print ("2: Guest names")
        print ("3: Update guest list")
        
        choice = input("Please make a selection: ")
            
        if choice == "1":
            (get_participant_count.total_customer_count(name))
            
            
            
        elif choice=="2":
            print ("The guest list is: ")
            print(name)
            
            
        elif choice =="3":
            
            add_participant.update_participant(name)
            #updated_list(new_name)
            
    
                
                
        else:
            print("Invalid selection")
            
            
            
            
            
main()
                
            
        