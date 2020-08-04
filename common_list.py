'''Write a python program that takes two lists and if they have at least one 
common member and print the odd number of the last list.'''
list_one = []
list_two = []
def insert_list():
    sizel1 = int(input("Enter size of lists : "))    
    for i in range(sizel1):
        strs = int(input("enter value [{}] to list_one :".format(i)))
        list_one.append(strs)
    print("===========================================")
    for i in range(sizel1):
        strs = int(input("enter value [{}] to list_two :".format(i)))
        list_two.append(strs)
    print("==========================================")    
    print("list_one is : {} ".format(list_one))
    print("list_one is : {} ".format(list_two))
def compare():
    flag = False
    for x in list_one:
       for y in list_two:
           if x == y:
               flag = True 
    return flag
def odd_mem():
    for n in list_two:
        if n%2 != 0:
            print(n)
def main():
    insert_list()
    print("Common member in list_two {}".format(compare()))
    print("Odd member in list_two is : ")
    odd_mem()
    
main()
