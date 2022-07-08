from cs50 import get_int

# Take for user input
while True:
    height = get_int("Height: ")
    width = height + 1
    if height > 0 and height <= 8:
        break

# Print a loop
for i in range(1, height + 1):
    num_hashes = i + 1
    num_spaces = width - num_hashes

    print(" " * num_spaces, end="")
    print("#" * i)