def outer():

    print("outer function started")

    def inner():
        print("Inner function")
    
    return inner
    #return "Rahul"
    #return 100
    

result=outer()

print(type(result))
result()  #function is callable
result()  #function is callable
result()  #function is callable
result()  #function is callable
result()  #function is callable
result()  #function is callable
result()  #function is callable
result()  #function is callable
result()  #function is callable