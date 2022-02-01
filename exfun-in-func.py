def myfunc():
    x = 300
    y = 2
    def myinnerfunc():
        print(x*2*y)
 
    myinnerfunc()
    print(x**y/2)
myfunc()