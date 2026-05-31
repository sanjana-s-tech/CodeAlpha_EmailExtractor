import re

print("===== EMAIL EXTRACTOR =====")

try:
    with open(r"C:\Users\s sanjana\OneDrive\Desktop\CodeAlpha_EmailExtractor\input.txt", "r") as file:
        text = file.read()

    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    with open("extracted_emails.txt", "w") as output:
        for email in emails:
            output.write(email + "\n")

    print("\nEmails Found:")
    for email in emails:
        print(email)

    print("\nEmail extraction completed successfully!")

except FileNotFoundError:
    print("input.txt file not found.")