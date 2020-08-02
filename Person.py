#create person class and display name and address using OOP concept
class Person(object): #creates a class of person
    # method to add name, address and phone
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
    # method to display the attribute of Person
    def display(self):
        return f"Name : {self.name} \n Address : {self.address} \n Phone : {self.phone}"
    #creating object of the class 
person1 = Person("Jagriti", "Kathmandu","980#######")
person2 = Person("Jags", "Lalitpur","980########")
    #accessing object of the class
print(person1.display())
print(person2.display())
    