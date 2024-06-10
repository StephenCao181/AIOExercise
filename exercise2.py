import math

# Function to check if a value is a number
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
        print("X must be a number")

# sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Relu funciton
def relu(x):
    return max(0, x)

# Elu fuction
def elu(x, alpha=0.01):
    if x >= 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)

# Main function to process the input
def activation_function(x, func_name):
    if not is_number(x):
        print('x must be a number')
        return

    x = float(x)

    if func_name == 'sigmoid':
        return sigmoid(x)
        print(f'sigmoid: f({x})={result}')
    elif func_name == 'relu':
        return relu(x)
        print(f'relu: f({x})={result}')
    elif func_name == 'elu':
        return elu(x)
        print(f'elu: f({x})={result}')
    else:
        print(f'{func_name}  is not supported')
        return

x = input("Enter the value of x: ")
func_name = input("Enter the activation function name (sigmoid, relu, elu): ")
activation_function(x, func_name)
