import math
x1=int(input("Enter the distance x1"))
x2=int(input("Enter the distance x2"))
y1=int(input("Enter the distance y1"))
y2=int(input("Enter the distance y2"))
distance=math.pow((x2-x1),2)+math.pow((y2-y1),2)
result=math.sqrt(distance)
print(f"The ecludi distance is:{result}")