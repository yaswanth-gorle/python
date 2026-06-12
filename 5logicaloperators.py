# In Python, 'and' returns the first falsy value, 
# or the last value if all are truthy.
# Since 10 is truthy, it evaluates and returns the second value (20).
a = 10 
b = 20
result = a and b 
print(result)  # Outputs: 20

# In Python, 'or' returns the first truthy value it encounters.
# Since 15 is truthy, it immediately returns 15 without looking at y.
x = 15
y = 20
result_or = x or y
print(result_or)  # Outputs: 15




