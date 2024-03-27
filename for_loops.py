def vowel_counter():
    """ counts and checks for vowels within a word
    """
    word = input("Enter a word to check for vowels: ")
    vowel_list = []
    word = word.lower()
    vowels = "aeiou"
    for letter in word:
        if letter in vowels:
            vowel_list.append(letter)
    print(f"Num of vowels in the word {word} is {len(vowel_list)}.")

vowel_counter()