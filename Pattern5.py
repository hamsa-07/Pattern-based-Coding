'''
Input Format: N = 3
Result: 
* * *
* * 
*

Input Format: N = 6
Result:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 
'''

def pattern(n):
    for i in range(n,0,-1):
        for j in range(1, i+1):
            print('*', end=" ")
        print()

n = int(input("Enter value:\n"))
pattern(n)
