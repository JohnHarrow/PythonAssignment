# Tasks:
# Read in the input file and store in some kind of data structure
# Generate three-letter abbreviations for each of the names based on the rules
# Genreate scores for each valid abbreviation based on rules
# Output the results 
import re
from collections import defaultdict

# Open File and store all the names
with open("Python Assignment/trees.txt", 'r') as file:
    names = [line.strip() for line in file.readlines()]


# Testing 
# names = ["Object-oriented programming", "Moore's Law", "Data Engineering", "Cool", "Cold", "C++ Code"] 

# Store letter values in dictionary
# Did not get aroung to using these
scores = {}
with open("Python Assignment/values.txt", 'r') as file2:
    for line in file2:
        letter, value = line.strip().split()
        scores[letter.upper()] = int(value)

# Create the abbreviations
def create_abbreviations(names):

    # Clean up the names recieved from the file
    def clean_name(name):
        # Remove apostrophes and split by non-alphabet characters
        name = name.replace("'", "")  # Remove the apostrophes
        words = re.split(r'[^A-Za-z]+', name)  # Split by non-alphabet characters
        return [word.upper() for word in words if word]  # Remove empty words and make uppercase

    # Take the cleaned up works and create abbreviations
    def generate_abbreviation_from_words(words):
        abbreviations = [] # Create empty list
        for word in words: # Loop through each word
            # For each word, generate all combinations of the first letter plus 2 more letters
            for i in range(1, len(word)): # Start loop from second letter to second last letter
                for j in range(i + 1, len(word)): # Loop starts from the letter after i
                    abbreviations.append(word[0] + word[i] + word[j]) # Combbines the first letter of the word plus the letters at positions i and j
        return abbreviations

    # Dictionary to store all abbreviations for each name
    names_to_abbrs = defaultdict(list)

    # Loop through each name, clean the name, create all the abbreviations for the name, store the abbreviations for each name
    for name in names:
        words = clean_name(name) # Clean the name
        abbrs = generate_abbreviation_from_words(words) # Create abbreviations for the name
        names_to_abbrs[name].extend(abbrs)  # Store all abbreviations for the name

    # Output all abbreviations for each name
    resulting_abbreviations = [] # Create list
    for name, abbrs in names_to_abbrs.items(): # Loops through each name and its list of abbreviations
        resulting_abbreviations.append(f"{name}: {' '.join(sorted(abbrs))}") # Fromat output to have the name and all the abbreviations sorted alphabetically seperated by a space
    
    return resulting_abbreviations

# Create the abbreviations
abbreviations = create_abbreviations(names)

# Print all of the abbreviations to a file
with open("Python Assignment/output.txt", 'w') as file:
    for abbr in abbreviations:
        file.write(abbr + "\n")

