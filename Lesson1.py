from pip._vendor.distlib.compat import raw_input

number = int(raw_input("Number: "))
print(number)
if number > 5:
    print("Number is greater than 5")
elif number < 5:
    print("Number is less than 5")
else:
    print("Number is equal to 5")
