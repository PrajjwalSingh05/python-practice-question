num1=int(input("Enter a number:"))
newnum=0
num=num1
while(num1>0):
    rem=num1%10
    newnum=rem+newnum*10
    num1=num1//10
print(f"The original value is {num} and reverse is {newnum}")