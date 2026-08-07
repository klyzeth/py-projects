print("-----------------------------------------")
print("--------------- CALCULATOR ----------------")
print("-----------------------------------------")

expression = input("Enter operation (+, -, *, /) or type 'e' to exit: ")

if expression == "e":
    print("Exiting the calculator.")
    exit()


op1 = float(input("Enter first number: "))
op2 = float(input("Enter second number: "))


if expression == "+":
    output = op1 + op2
    print("Result: ", output)

elif expression == "-":
    output = op1 - op2
    print("Result: ", output)

elif expression == "*":
    output = op1 * op2
    print("Result: ", output)

elif expression == "/":
    output = op1 / op2
    print("Result: ", output)


else:
    print("INVALID INPUT")