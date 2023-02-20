total = 0
count = 0

while count < 5:
    try:
        num = int(input(f"Enter int #{count+1}: "))
        total += num
        count += 1
    except ValueError:
        print("Invalid input. Please enter an int.")

print(f"Your sum is {total}")
