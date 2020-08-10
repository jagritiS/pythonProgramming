#Calculate total price based on the stock bought by the customer 
def inputs():
    days = int(input("Enter days : "))
    customer = int(input("Enter customer id : "))
    cstm =[]
    stocks = []
    unts = []
    cstm.append(customer)
    tuples = (customer,days,stocks,unts)
    stck(tuples)
def stck(tuples):
    for x in range(20):
        print("cutomer id :",tuples[0])
        sums =0
        for i in range(tuples[1]) :
            stck = int(input("Enter stock for day {} : ".format(i)))
            tuples[2].append(stck)
            units = int(input("Enter unit : "))
            tuples[3].append(units)
            prd = units*stck       
            sums = sums+prd            
            print("day {} charge {} : ".format(i,sums))
            calDiscount(sums)
        print("---------------------------------------")
        sums  = 0
        cust = list(tuples)
        cust[0] = cust[0]+1
        tuples = tuple(cust)
def calDiscount(sums):
    extras = 0
    total = 0
    disTuple = (0.10,0.15,0.25)
    if(sums<200):   
        total = sums     
    elif sums >200 and sums <400:
        total = sums - (sums *disTuple[0])
    elif sums >400 and sums <800:
        total = sums - (sums * disTuple[1])
    else :
        total = sums - (sums * disTuple[2])       
    display(total)
def display(totals):    
    print("Charge after discout is .",totals)
def main():
    inputs()    
main()
