'''Write a Python program to count Uppercase, Lowercase, 
special character and numeric values in a given string.'''
strs = []
strs = input("Enter a string :")
print("The string is : ",strs)
def count(strs):
    low = 0
    upr = 0 
    nm = 0
    spcl = 0
    for i in strs:
        if(i>='a' and i<='z'):
            low +=1
        elif(i>='A' and i<='Z'):
            upr +=1
        elif(i>='0' and i<='9'):
            nm +=1
        else:
            spcl +=1
    print("Uppercase : {}, lowercase :{}, numeric : {}, special character : {}".format(upr,low,nm,spcl))
def main():
    count(strs)
main()