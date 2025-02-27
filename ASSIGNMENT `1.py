#leap and not leap year
year = int(input("Enter a year: "))  # Take input from the user

# Check leap year conditions
if (year % 4 == 0 and year % 100 != 0):  
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#marks

marks = int(input("Enter your marks: ")) # Take marks as input

# Check grade based on marks
if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
elif 60 <= marks <= 69:
    print("Grade: D")
else:
    print("Grade: F")

#operator +=
num = 5   
num += 10
print(num) 
# Output: 15


