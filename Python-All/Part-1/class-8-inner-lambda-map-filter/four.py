def user_details():

    def login():
        print("Login success")

    def logout():
        print("Logout success")

    def get_user():
        return "Rahul"
    #return 100,200
    return login,logout
    
result=user_details()
print(result)
result[0]()
result[1]()