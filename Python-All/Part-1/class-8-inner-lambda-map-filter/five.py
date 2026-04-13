def calcate():
    print("calcate function")

    def sum():
        print("sum function")

    sum()

    def multi():
        print("multi function")

    multi()       #involing innner function
    return multi  #retunr inner fun-ref

result=calcate()
result() #involing inner fun -multi from outside