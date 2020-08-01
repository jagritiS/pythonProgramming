# while --> break, pass and continue 
i = 1
while i<6 :
    print("i = ",i)
    if i == 3 :
        break # breaks the loop after i reaches 3 
    i += 1
print("=================================")    
j =1
while j <6 :
    print("j = ",j)
    if j == 3 :
        pass # pass --> it passes to the next value   
    j += 1  
print("=================================") 
k = 0 
while k < 6 :
    k += 1    
    if k == 3 :
        continue   # continue --> it omits the true condition and moves towards the next 
    print("k = ",k)  