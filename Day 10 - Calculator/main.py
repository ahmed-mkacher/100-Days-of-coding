def addition(n1, n2):
  return n1+n2

def multiplication(n1, n2):
  return n1*n2

def division(n1, n2):
  return n1/n2

def substraction(n1, n2):
  return n1-n2

operations = {
              "+":addition,
              "-":substraction,
              "/":division,
              "*":multiplication
            }

num1 = int(input("Pick a number:  "))
operation = input("What operation do you want? Please choose between '+','*','-','/'  ")
num2 = int(input("Pick another number:  "))

calculation = operations[operation]
print(f"{num1} {operation} {num2} = {calculation(num1, num2)}")