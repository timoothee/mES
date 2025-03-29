target_value = 7 
list_values = [2, 5, 9, 11, 14] 
closest_value = min(list_values, key=lambda x: abs(x - target_value))
print(f"The closest value to {target_value} is {closest_value}")
print(list_values.index(closest_value))