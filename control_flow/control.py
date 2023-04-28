   # Write a function that uses while, if and continue statements to print all the even
#  numbers between 0 and 50. 
def even_nums():
     k = 0
     while k <= 50:
        if k % 2 != 0:
            k += 1
            continue
        print(k)
        k += 1

    # Write a function that takes an integer argument and prints "Prime" if the number is prime,
    #  and "Not prime" if the number is not prime.
def is_prime(k):
    if k <= 1:
        print("Not a prime number")
        return
        i = 0:
    for i in range(2, int(k/2)+1):
        if k % i == 0:
            print("Not a prime number")
            break
    else:
        print("It's a prime number")
# Write a function that takes a list of integers as input and prints the sum of 
# all the even numbers in the list.
def sum_even(nums):
    sum_even=0
    for j in nums:
        if j%2==0:
           sum_even+=j
    print(sum_even)

# Write a function that takes any two integers as input, and prints the 
# sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_divisible_by_three(num1, num2):
    total = 0
    for num in range(min(num1, num2), max(num1, num2) + 1):
        if num % 3 == 0:
            total += num
    print("The sum of all numbers between", num1, "and", num2,
     "that are divisible by 3 is:", total)


