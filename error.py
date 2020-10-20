result = None
x = int(input("number 1:"))
y = int(input("number 2:"))


try:
    result = x / y
except Exception as e:
    print(e)
else:
    print("inside else block")
finally:
    print("inside finally")
print("--New line ")
print("result = ", result)