def user_details():
    print("user details - outer function started")

    def login():
       print("Login success") 

    def logout():
        print("Logout success") 

    login()
    logout()


user_details()