try:
    with open("input.txt", "r") as infile:
        lines = infile.readlines()

    with open("output.txt", "w") as outfile:
        for i, line in enumerate(lines, start=1):
            outfile.write(f"{i}: {line}")

    print("Modified file saved as output.txt")

except FileNotFoundError:
    print("File not found.")

except IOError:
    print("Error reading or writing file.")
