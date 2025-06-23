import re

# Input and output file paths
input_file = "emails_input.txt"
output_file = "emails_output.txt"

# Read file content
with open(input_file, 'r') as file:
    content = file.read()

# Find all email addresses
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

# Write emails to output file
with open(output_file, 'w') as file:
    for email in emails:
        file.write(email + '\n')

print(f"\nExtracted {len(emails)} email(s) to '{output_file}'.")
