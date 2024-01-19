while True:
    try:
        num1 = int(input ("Enter first number: "))
        num2 = int(input ("Enter second number: "))
        num3 = int(input ("Enter third number: "))
        break
    except Exception:
        print("Invalid input. Please enter an integer.")

if num1>num2 and num1>num3:
    g1 = num1
elif num2>num1 and num2>num3:
    g1 = num2
else:
    g1 = num3
print ("The largest number is:",g1)