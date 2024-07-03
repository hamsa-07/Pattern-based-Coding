'''
Input Format: N = 3
Result: 
1
01
101

Input Format: N = 6
Result:   
1
01
101
0101
10101
010101
'''

def pattern(n):
    for i in range(1, n+1):
        if i % 2 == 1:
            print('1'+'0' * (i-1))
        else:
            print('0'+'1'*(i-1))
        

n = int(input("Enter size:\n"))
pattern(n)