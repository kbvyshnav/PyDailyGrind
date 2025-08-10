'''-----program to find prime numbers from 1 to 100-------'''

#Using method of Check divisors only up to the square root:
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

#Using two pointer method :
left = 2
right = 100

while left <= right:
    # Check if left is prime
    for i in range(2, int(left ** 0.5) + 1):
        if left % i == 0:
            break
    else:
        print(left)

    # If left == right, avoid duplicate check (when pointers meet in the middle)
    if left != right:
        for i in range(2, int(right ** 0.5) + 1):
            if right % i == 0:
                break
        else:
            print(right)
    left += 1
    right -= 1
        



#check if a number i prime number or not.
num=int(input("Enter a number :  "))
count=0

for i in range (1,num+1):
    if num%i==0:
        count=count+1

if count ==2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")    


    
if count ==2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")    

