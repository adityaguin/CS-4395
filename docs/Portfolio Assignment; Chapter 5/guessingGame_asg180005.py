import random
import sys
from nltk.corpus import stopwords
from nltk import word_tokenize, WordNetLemmatizer, pos_tag


# Function to calculate the lexical diversity
def calculate_lexical_diversity():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        total_tokens = []
        for sentence in lines:
            current_sentence_tokens = word_tokenize(sentence)
            for token in current_sentence_tokens:
                total_tokens.append(token)
        unique_tokens = set(total_tokens)
        return "{:.2f}".format(len(unique_tokens) / len(total_tokens)), total_tokens


# Preprocess the raw text
def preprocess_raw_text():
    # 3a. Getting total tokens and preprocessing it
    unprocessed_total_tokens = calculate_lexical_diversity()[1]
    preprocessed_tokens = [t.lower() for t in unprocessed_total_tokens if len(t) > 5 and t.isalpha()
                           and t not in stopwords.words('english')]

    # 3b. Creating unique set of lemmas from preprocessed text
    lemmer = WordNetLemmatizer()
    lemmatized = [lemmer.lemmatize(token) for token in preprocessed_tokens]
    unique_lemmas = set(lemmatized)

    # 3c. POS Tagging on lemmas
    pos_tagged_unique_lemmas = pos_tag(unique_lemmas)
    print()  # Ease of reading output
    print("First 20 lemmas that are tagged")
    print(pos_tagged_unique_lemmas[:20])
    print()  # Ease of reading output

    # 3d. Only nouns
    lemmas_that_are_only_nouns = [lemma[0] for lemma in pos_tagged_unique_lemmas if lemma[1][:2] == 'NN']

    # 3e. Print the number of tokens and number of nouns
    print(f'Number of tokens: {len(preprocessed_tokens)}')
    print(f'Number of nouns: {len(lemmas_that_are_only_nouns)}')
    print()

    # Creating dictionary here
    noun_dictionary = dict()
    pos_tagged_tokens = pos_tag(preprocessed_tokens)
    for lemma in lemmas_that_are_only_nouns:
        noun_dictionary[lemma] = preprocessed_tokens.count(lemma)

    fifty_common_nouns = []
    print("Fifty most common nouns along with count")
    for k, v in sorted(noun_dictionary.items(), key=lambda item: item[1], reverse=True)[:50]:
        fifty_common_nouns.append(k)
        print(f'{k}, {v}')
    print()

    # 3f. Return number of tokens and nouns
    return len(preprocessed_tokens), len(lemmas_that_are_only_nouns), fifty_common_nouns

# Word bank is the fifty most common nouns. Word is chosen, and user has attempts to guess letter
# If points < 0, game ends. If user enters !, game ends.
# Points persist throughout multiple rounds of the game
def guessing_game(word_list):
    points = 5
    word_chosen = random.choice(word_list)
    # print(f'Word chosen {word_chosen}')
    letter_guessed = ''
    print(f'Lets play a guessing game!')

    guess_state = ['_' for i in range(len(word_chosen))]
    guessed_letters = []
    while letter_guessed != '!' and points >= 0:
        for thing in guess_state:
            print(thing, end=' ')
        print()
        letter_guessed = input("Guess a letter: ")

        if letter_guessed == '!':
            print("Exiting game now.")
            break

        epoint = False

    # Error checking. While user enters nonalpha character that isn't !, and also ensure user enters
        # only one character at at time
        while len(letter_guessed) != 1 or letter_guessed in guessed_letters or not letter_guessed.isalpha():
            while len(letter_guessed) != 1:
                letter_guessed = input(f'{letter_guessed} is not length 1! Guess another letter: ')
            while letter_guessed in guessed_letters:
                letter_guessed = input(f'{letter_guessed} already guessed! Guess another letter: ')
            while not letter_guessed.isalpha():
                if letter_guessed == '!':
                    epoint = True
                    break
                letter_guessed = input(f'{letter_guessed} is not an alphabet! Guess another letter: ')
            if letter_guessed == '!':
                print("Exiting game now.")
                epoint = True
                break

        if epoint:
            break
        letter_guessed = letter_guessed.lower()
        guessed_letters.append(letter_guessed)
        if letter_guessed in word_chosen:
            points += 1
            print(f'Right! Score is {points}')
            for idx, char in enumerate (word_chosen):
                if char == letter_guessed:
                    guess_state[idx] = char
        else:
            points -= 1
            print(f'Sorry, guess again. Score is {points}')
        if guess_state == list(word_chosen):
            print(f'CONGRATS! You have guessed the {word_chosen}. New word has been chosen')
            print()
            word_chosen = random.choice(word_list)
            guess_state = ['_' for i in range(len(word_chosen))]
            guessed_letters.clear()

    if points < 0:
        print()
        print(f'Your score is less than 0 ({points} points). The word chosen was {word_chosen}')


if __name__ == "__main__":
    # Error checking for file name to textfile in sysarg
    if len(sys.argv) < 2:
        print('Filename for text not given in sysarg. Program ending')
    else:
        print(f'Lexical Diversity (2 decimals): {calculate_lexical_diversity()[0]}')
        tokens, nouns, fifty_common_nouns = preprocess_raw_text()
        guessing_game(fifty_common_nouns)
