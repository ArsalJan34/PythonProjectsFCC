def audit_allocation(total_funds, split_count):
  try:
    result = int(total_funds/split_count)
  except ZeroDivisionError:
    print("Error! ")
    return "Error Encountered."
  else:
    print(f"Result is {result}")
  finally:
    print("Execution complete!")

print("---Runnign test 2 (error state ) ------ ")
audit_allocation(100,4)
print("\n--- Running Test 2 (Error State) ---")
audit_allocation(100, 0)
