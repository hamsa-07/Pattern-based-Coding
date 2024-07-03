'''
        PATTERN TYPE 3
Input Format: N = 3
Result: 
1
1 2 
1 2 3

Input Format: N = 6
Result:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
'''
def pattern(n):
    for i in range(1, n+1):
        print()
        for j in range(1, i+1):
            print(j, end=" ")
    
n = int(input("Enter a value:\n"))
pattern(n)
