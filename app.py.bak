import pandas
from functions import *

"""
20 24 Dec 2024
"""


def create_phonetic_list():
    """This creates phonetic list of word entered by the user."""
    word = input("Enter a word: ").upper()
    try:
        phonetic_list = [data_dict[letter] for letter in word if letter != " "]
    except KeyError:
        print("Please enter alphabets only.")
        create_phonetic_list()
    except NameError:
        print("Please enter alphabets only.")
        create_phonetic_list()
    else:
        print(phonetic_list)
    finally:
        print("Program Completed")


# Here we are reading data from .csv file and converting it to dictionary using dictionary comprehension
print(logo)
df = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in df.iterrows()}

on = True
while on:
    # Here based on word entered by user we are making phonetic word list
    create_phonetic_list()

    print("")

    # Asking user whether they want to continue to generate the phonetic words or not ?
    want_to_generate = input("Do you want to generate again ? type (Y/N)").upper()
    if want_to_generate == "Y":
        print("\n" * 25)
        print(logo)
        continue
    else:
        print("Exiting the program, Goodbye!")
        name_l()
        on = False
