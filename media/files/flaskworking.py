'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
class App():
    def __init__(self):
        self.x =45
        self.y = 22
        self.z ={}
    def specai(self , u):
        self.z[u] = 2*u
        def dec(func):
            self.z[u] = func
            
        return dec  
    def run(self):
        print(self.z)
        
app= App()

@app.specai("/this")        
def foo(req):
    print('fthign gghghh')
    
#print(s.z)   

app.run()
# this probably how flask app works , inside of run() method in the class there must be some network programming to listen to request 
#and forward those requst to the appropriate function
    