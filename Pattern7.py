'''
Input Format: N = 3
Result: 
  *  
 *** 
*****   
Input Format: N = 6
Result:
     *     
    ***    
   *****   
  *******  
 ********* 
***********
'''

def pattern(n):
    
    for i in range(1, n+1):
        for j in range(n - i ):
            print(' ',end="")
        for j in range(2 * i -1):
            print('*', end="")
        print()
    

n=int(input("Entersize:\n"))
pattern(n)