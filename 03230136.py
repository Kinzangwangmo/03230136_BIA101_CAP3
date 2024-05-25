#
# Kinzang Wangmo
#BBI'B'
#03230136
#References

#SOLUTION
# Total Sum = 224610

def read_input():
  """Reads the contents of the '136.txt' file.

  Returns:
    A string containing the contents of the file, or an empty string if the file is not found."""
  try:
    with open("136.txt", "r") as f:
      content = f.read()
      return content
  except FileNotFoundError:
    # File not found, return an empty string
    return ""

# Call the read_input function
content = read_input()

# Process the content
if content:
  print("Content of 136.txt:", content)
else:
  print("File '136.txt' not found.")

filename = "136.txt"
with open(filename, "r") as f:
  total_sum = 0  # Initialize total_sum inside the block
  for line in f:
    # Check if line is empty
    if not line:
      continue

    # TO get first and last digits 
    first_digit = int(line[0]) if line[0].isdigit() else 0
    last_digit = int(line[-1]) if line[-1].isdigit() else 0

    # Combine and add to get total sum
    total_sum += first_digit * 10 + last_digit

print(f"Sum of combined first and last digits: {total_sum}")

