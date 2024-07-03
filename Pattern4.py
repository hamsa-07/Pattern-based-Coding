'''
        PATTERN TYPE 4
Input Format: N = 3
Result: 
1
2 2 
3 3 3

Input Format: N = 6
Result:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
'''

def pattern(n):
    for i in range(1, n+1):
        print()
        for j in range(1, i+1):
            print(i, end=" ")

n = int(input("Enter value:\n"))
pattern(n)