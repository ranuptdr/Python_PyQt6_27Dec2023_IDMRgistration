# class defination
class MyClass():
    #1 property

    #2 constructor

    #3 method/function
    def cursor(self):
        pass
    pass
# class external object = ClassName() 
ceo = MyClass() # if a variable defination ourside the  function global
# funtion defination is a one time process
def connect(dbname):
    #return 1 # every function return something
    return ceo
    pass

x = 10 # global veriable
# funtion defination is a one time process
def add():
    y = 20 # Local veriable 
    print(x+y)
    pass
# function calling is a many time process
add() 
