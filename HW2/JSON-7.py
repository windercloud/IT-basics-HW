import json

value = 2 + 5j 
if isinstance(value, complex):
    print(f"{value} is complex")
else:
    print(f"{value} is not complex")
