# CodeAlpha_EmailExtractor
A Python automation script that extracts email addresses from a text file using regular expressions and saves them to a separate output file.
# Email Extractor

## Project Overview

Email Extractor is a Python automation script that reads a text file, identifies valid email addresses using Regular Expressions (Regex), and saves the extracted emails into a separate output file.

This project demonstrates the use of Python for automating repetitive tasks involving text processing and data extraction.

---

## Features

- Reads data from a text file
- Extracts valid email addresses automatically
- Uses Regular Expressions (Regex) for pattern matching
- Saves extracted emails to a separate text file
- Displays extracted emails in the terminal
- Simple and beginner-friendly automation project

---

## Technologies Used

- Python
- Regular Expressions (re module)
- File Handling

---

## Project Structure

```text
CodeAlpha_EmailExtractor
│
├── email_extractor.py
├── input.txt
├── extracted_emails.txt
└── README.md
```

---

## How It Works

1. The script reads the content of `input.txt`.
2. It searches for valid email addresses using Regex.
3. All detected email addresses are extracted.
4. The extracted emails are stored in `extracted_emails.txt`.
5. The results are displayed in the terminal.

---

## Sample Input

```text
Welcome to CodeAlpha Internship Program

For support:
support@codealpha.tech

For internship queries:
internships@codealpha.tech

Business Contact:
business@yahoo.com
```

---

## Sample Output

```text
support@codealpha.tech
internships@codealpha.tech
business@yahoo.com
```

---

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python email_extractor.py
```

4. Check the generated `extracted_emails.txt` file.

---

## Learning Outcomes

Through this project, I learned:

- Python file handling
- Automation scripting
- Regular Expressions (Regex)
- Pattern matching techniques
- Data extraction from text files

---

## Author

Developed as part of the **CodeAlpha Python Programming Internship**.
