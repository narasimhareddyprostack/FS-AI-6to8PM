try:
    with open("data.txt", "r") as fp:
        data = fp.read()
        print(data)

except FileNotFoundError as err:
    print("Error:", err)

finally:
    print("Finally block will execute always")

print("GE")