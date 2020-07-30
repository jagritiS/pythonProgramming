'''If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''

multiple_sum = 0
def mult_sum(nums):
    for i in range(1000):
        if (i%3 == 0 or i%5 == 0):
            nums = nums+i
    print("The sum of all multiples of 3 and 5 below 1000 is : ",nums)
def main():
    mult_sum(multiple_sum)
main()