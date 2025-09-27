
# номер який нам дає користувач
num1 = float(input("Enter first number: "))
# користувач вводить операцію
operation = (input("Enter operation: (*, /, -, +):  "))
# вводить другий номер
num2  = float(input("Enter second number: "))

#види обчислень
if operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "+":
    print(num1 + num2)
# якщо такої операції немає
else:
    print("Invalid operation")


