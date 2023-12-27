import math
def square(num):
    answer=0

    while(num>0):
        rem=num%10
        answer=answer+pow(rem,2)
        num =num//10
    return answer



num=int(input("Enter the number:"))
ans=square(num)
print(f"The square of the digit is :{ans}")