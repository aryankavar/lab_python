try:
    my_list = [1, 2, 3]
    print(my_list[1])  # This will raise an IndexError
except IndexError as e:
    print(f"Error: {e}")
else:
    print("element accessed successfully.")
finally:
    print("Execution completed.")