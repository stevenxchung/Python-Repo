# Add
def add(x, y):
  return x + y

# Subtract
def subtract(x, y):
  return x - y

# Multiply
def multiply(x, y):
  return x * y

# Divide
def divide(x, y):
  if y == 0:
    raise ValueError("Can not divide by zero!")
  return x / y
