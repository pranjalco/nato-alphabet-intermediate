---
# Project 20: NATO Alphabet

## Author
- **Name**: Pranjal Sarnaik
- **Date Created**: 24 Dec 2024

---

## Description
This program generates a NATO phonetic list for a word entered by the user. It uses the `create_phonetic_list()` function to achieve this functionality. Key features of the program include:
- Input validation using `try`, `except`, `else`, and `finally` blocks.
- Integration with the `pandas` library to read data from the `nato_phonetic_alphabet.csv` file and convert it into a dictionary containing letters and their corresponding NATO phonetic codes.
- Use of dictionary comprehension for efficient data processing.
- Interactive functionality to allow the user to continue generating phonetic lists or exit the program.

---

## How to Use
1. **Run the Program:**
   - The user inputs a word.
   - The program outputs the NATO phonetic equivalent of each letter in the word.
2. **Continue or Exit:**
   - After the phonetic list is generated, the program asks the user whether they want to continue.
   - If the user opts to continue, they can input another word.
   - If not, the program stops execution.

---

## Level
- **Level**: Intermediate
- **Skills:** Python Basics, Error Handling, Pandas, File Handling, Dictionary Comprehension
- **Domain**: Educational/Utility

---

## Features
- Generates a NATO phonetic list for user-entered words.
- Validates user input for correct data entry.
- Reads and processes data from a CSV file.
- Allows users to repeat or exit the program interactively.
- Includes modular design with functions for clarity and reusability.

---

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/pranjalco/nato-alphabet-intermediate.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd nato-alphabet-intermediate
   ```

---

## Running the Program
1. **Prerequisites:**
   - Ensure Python 3.9 or later is installed on your system.
   - Install required libraries using:
     ```bash
     pip install pandas
     ```

2. **Execute the Program:**
   - **Using PyCharm:** Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt:** Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking:** Double-click `app.py` to run it directly, provided Python is configured to execute `.py` files.

3. **Troubleshooting:**
   - If the console window closes immediately, run the program via terminal/command prompt or an IDE to view the output.

---

## File Structure
- **`nato_phonetic_alphabet.csv`:** Contains the NATO phonetic alphabet data.
- **`app.py`:** Main program file.
- **`experiments/`:** Folder containing temporary or practice files.
- **`screenshots/`:** Folder containing screenshots of the program.

---

**Created by Pranjal Sarnaik**  
*© 2024. All rights reserved.*

