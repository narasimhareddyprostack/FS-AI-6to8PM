try:
    a=int(input("Enter First Number:")) 
    b=int(input("Enter Second Number:")) 
    c=eval(input("Enter Third Number:"))
    print(a/b)        
    print(a+c)

except TypeError as err:
    print(err) 

except ValueError as err:
    print(err) 

except ZeroDivisionError as err:
    print(err)

except Exception as err:
    print("Check the Error Hierarchy")
    print(err)

print("GE")