'''
Input Format: N = 3
Result: 
  *  
  **
  ***  
  **
  *   
Input Format: N = 6
Result:   
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *
'''

def pattern(n):
  for i in range(1, n+1):
    for j in range(1, i+1):
      print('*', end=" ")
    print()
    
def inverted(n):
  for i in range(n-1,0,-1):
    for j in range(i,0,-1):
      print('*', end=" ")
    print()
  
n = int(input("Enter size:\n"))
pattern(n)
inverted(n)