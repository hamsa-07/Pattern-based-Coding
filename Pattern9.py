'''
Input Format: N = 3
Result: 
  *  
 ***
***** 
*****  
 ***
  *   
Input Format: N = 6
Result:   
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *
'''

def pattern(n):
    for i in range(1, n+1):
        for j in range(n - i ):
            print(' ',end="")
        for j in range(2 * i -1):
            print('*', end="")
        print()
        
def inverted(n):
    for i in range(n,0,-1):
        for k in range(n-i):
            print(' ', end="")
        for k in range(2*i-1):
            print('*', end="")
        print()

n = int(input("Enter size:\n"))
pattern(n)
inverted(n)