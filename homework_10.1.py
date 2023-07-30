import random
import string

def generate_random_numbers_and_create_files():
    with open("summary.txt", "a") as summary:  # Apriamo il file "summary.txt" in modalità di append
        for letter in string.ascii_uppercase:
            filename = letter + ".txt"
            number = random.randint(1, 100)
            with open(filename, "w") as file:
                file.write(str(number))
            # Aggiungiamo una riga al file "summary.txt" contenente il nome del file e il numero casuale
            summary.write(f"{filename}: {number}\n")

generate_random_numbers_and_create_files()