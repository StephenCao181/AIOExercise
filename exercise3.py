import random
import math

#Calculate MAE, MSE and RMSE
def calculate_loss(loss_name, num_samples):
    if not num_samples.isnumeric():
        print('Number of samples must be an integer number')
        return
    
    num_samples = int(num_samples)
    
    y = [random.uniform(0, 10) for _ in range(num_samples)]
    y_hat = [random.uniform(0, 10) for _ in range(num_samples)]
    
    print(f"Loss name: {loss_name}")
    for i in range(num_samples):
        y1 = y[i]
        y2 = y_hat[i]
        if loss_name == 'MAE':
            loss = abs(y1-y2)
        elif loss_name == 'MSE':
            loss = (y1-y2) ** 2
        elif loss_name == 'RMSE':
            loss = math.sqrt((y1-y2) ** 2)
        
        print(f"Sample-{i}: y = {y1}, y_hat = {y2}, loss = {loss}")

# User input
num_samples = input("Enter the number of samples: ")
loss_name = input("Enter the loss name (MAE, MSE, RMSE): ")

# Calculate and print loss
calculate_loss(loss_name, num_samples)
