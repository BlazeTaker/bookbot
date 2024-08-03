def main(book):
    with open(book) as f:
        file_contents = f.read()

def countWords(book):
    count = 0

    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
    
    for word in range(0,len(words)):
        count += 1

    return count

def countCharacter(book):
    character_dict = {}
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()

        for word in words:
            lowered_string = word.lower()
            for char in lowered_string:
                if char in character_dict:
                    #take the current value and increment by 1
                    character_dict[char] += 1
                elif char not in character_dict:
                    #add current character in dict
                    character_dict[char] = 1
    sorted_keys = sorted(character_dict.keys())
    sorted_dict = {key: character_dict[key] for key in sorted_keys}
    return sorted_dict


path = ("books/frankenstein.txt")

main(path)
print(f"--- Heya friend, here's what I found in {path} ---")
print(f"This book has {countWords(path)} words")
charCount = countCharacter(path)
char = ""

for char in charCount:
    if char.isalpha() == True:
        print(f"{char} appears {charCount[char]} times")

