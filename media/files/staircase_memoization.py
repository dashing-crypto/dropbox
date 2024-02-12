'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def climb(n , d={}):
            if n in d:
                return d[n]
            
            if n == 1 or n == 0:
                return 1
            if n == 2:
                return 2
            d[n] = climb(n-1 ,d) +climb(n-2 ,d)   # this works even if we do not pass d in these two calls
            return d[n] 
            
            

           
print(climb(5))
#how is this above memoization working , we are not even passing the d in the climb call
#it is beacuse we are passing the same d in all the recursive calls, we may not be passing it explicityly but it is being used by recuresed function beacuse it is in the scope 