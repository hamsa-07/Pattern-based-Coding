'''
        PATTERN TYPE 2:
Input Format: N = 3
Result: 
* 
* * 
* * *

Input Format: N = 6
Result:
* 
* * 
* * *
* * * *
* * * * *
* * * * * *
'''

def pattern(n):
    for i in range(1,n+1):
        print()
        for j in range(1, i+1):
            print('*', end=" ")     

n = int(input("Enter size:\n"))
pattern (n)
array = []
