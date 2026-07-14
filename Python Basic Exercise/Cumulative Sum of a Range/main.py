# my code
print("Printing current and previous number sum in a range(10)")
for i in range(1,11):
  previous = i - 1
  sum = i + previous
  print(f"current Number {i} Previous number {previous} Sum : {sum} ")

# solution---------------
print("Printing current and previous number sum in a range(10)")

# Start with the previous number set to 0
previous_num = 0

# Loop through numbers 0 to 9
for i in range(10):
    total_sum = i + previous_num
    print(f"Current Number {i} Previous Number {previous_num} Sum: {total_sum}")

    # Update previous_num to be the current number for the next iteration
    previous_num = i
