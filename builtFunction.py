#python built in functon used in string 
strs = " This, is, a ,test, function, "
print("Given String is = ",strs)
print("length of string strs = ",len(strs))
print("removing whitespace from begining and end = ",strs.strip())
print("String in lower case = ",strs.lower())
print("String in upper case = ",strs.upper())
print("Replacing t by k = ",strs.replace('T','K'))
print("Spliting comma = ",strs.split(","))
# check the following string is in above or not 
x = "his" in strs
print("The word 'his' is not in String strs = ",x)  # returns true if it contains the string
y = "aaim" not in strs 
print("aaim not in a = ",y)  # returns true if it doesnt contain the string 
# check uppercase       
print("String is in uppercase = ",strs.isupper())   #built in function isUpper to check whether the given string is uppercase or not 


