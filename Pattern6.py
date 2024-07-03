'''
Input Format: N = 3
Result: 
1 2 3
1 2
1

Input Format: N = 6
Result:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1
'''

def pattern(n):
    
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()
    
n=int(input("Enter size:\n"))
pattern(n)