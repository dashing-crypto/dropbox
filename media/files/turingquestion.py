'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
def game(ops :list):
    result =0
    score=[]
    for i , x in enumerate(ops):
        if x !="C" and x !="D" and  x !="+":
            score.append(int(x))
        if x =="C":
            score.pop()
        if x =="D":
            score.append(2*int(score[-1]))
        if x =="+":
            score.append(int(score[-1]) +int(score[-2]))
        #print(score)    
            
    return sum(score)  
   

print(game(["5","2" ,"C" ,"D" ,"+"]))

##turing.com practice test question
            
        
