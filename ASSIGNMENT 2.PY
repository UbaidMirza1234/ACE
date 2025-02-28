
# 1 no of triangle
def pascals_triangle(rows):
    for i in range(rows):
        # Print leading spaces for alignment
        print(" " * (rows - i - 1), end="")

        # Compute and print each row using the binomial coefficient formula
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)  # Compute next coefficient
        
        print()  # Move to the next line

# Example usage
pascals_triangle(5)



#2 continue function
for i in range(5):
    if i == 2:
        continue  # Skips when i = 2
    print(i)




 #3   Pythagorean triplets  
triplets = [(a, b, c) for a in range(1, 51) 
                      for b in range(a, 51) 
                      for c in range(b, 51) 
                      if a**2 + b**2 == c**2]

# Print the generated triplets
print(triplets)




#4 Consecutive number
def max_consecutive_sum(nums, k):
    if len(nums) < k or k <= 0:  
        return None  # Return None for invalid cases

    # Compute the sum of the first k elements
    max_sum = current_sum = sum(nums[:k])

    # Slide the window across the list
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]  # Add next element, remove first element of previous window
        max_sum = max(max_sum, current_sum)   # Update max_sum if new sum is larger

    return max_sum

# Example usage
nums = [2, 3, 5, 1, 6, 7, 2, 4]
k = 3
print(max_consecutive_sum(nums, k))  # Output: 14 (6+7+2)




#5 APPEND NEW ITEM
def modify_list(lst, item):
    lst.append(item)  # Modify the list by adding a new item
    print("Inside function:", lst)

# Example usage
my_list = [1, 2, 3]
modify_list(my_list, 4)

print("Outside function:", my_list)  # The change persists outside


#6  fibbonacci series
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Take user input
num = int(input("Enter the number of terms: "))

# Validate input
if num <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:", fibonacci(num))
