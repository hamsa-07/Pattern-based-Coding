'''
            PATTERN TYPE 1:
Example 1:
Input: N = 3
Output: 
* * *
* * *
* * *


Example 2:
Input: N = 6
Output:
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
'''

n = int(input("Enter size:\n"))

for i in range(n):
    for j in range(n):
        print('*', end=" ")
    print()