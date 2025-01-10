import pandas

# Here we are reading data from .csv file and converting it to dictionary using dictionary comprehension
df = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# data_dict = {}
# for index, row in df.iterrows():
#     data_dict[row.letter] = row.code

# print(data_dict)

on = True
while on:
    word = input("Enter a word: ").upper()

    # Here based on word entered by user we are making phonetic word list
    phonetic_list = [data_dict[letter] for letter in word if letter != " "]

    # phonetic_list = []
    # for letter in word:
    #     if letter != " ":
    #         phonetic_list.append(data_dict[letter])
    #     else:
    #         pass

    print(phonetic_list)

    print("")

    # Asking user whether they want to continue to generate the phonetic words or not ?
    want_to_generate = input("Do you want to generate again ? type (Y/N)").upper()
    if want_to_generate == "Y":
        print("\n" * 25)
        continue
    else:
        print("Exiting the program, Goodbye!")
        on = False




