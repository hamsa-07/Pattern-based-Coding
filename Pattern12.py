'''
Input Format: N = 3
Result: 
1    1
12  21
123321

Input Format: N = 6
Result:   
1          1
12        21
123      321
1234    4321
12345  54321
123456654321
'''

def pattern(n):
    
    space = 2*n
    
    for i in range(1, n+1):
        for j in range(1, i+1):
            print( j, end="")
            
        s = space - 2*i
        for j in range(s):
            print(' ', end="")
            
        for j in range(i,0, -1):
            print(j, end="")
        
        print()
    
n=int(input("Enter size:\n"))
pattern(n)