'''
Collaborators: Aditya Guin (asg180005), Varin Sikand (vss180000)
Date: 10/02/2022
CS 4395.001
'''
import os.path
import sys
from collections import Counter
from nltk import word_tokenize, ngrams
import pickle


def unigram_bigram_dict(file_name):
    print(file_name)
    with open(file_name, 'r', encoding='utf8') as f:
        raw_text = ' '.join([line.replace('\n', '') for line in f])
        unigrams_list = word_tokenize(raw_text)
        bigrams_list = list(ngrams(unigrams_list, 2))
        return Counter(unigrams_list), Counter(bigrams_list)



def main():
    if len(sys.argv) < 2:
        print('Filename for text not given in sysarg. Program ending')
    else:
        for file_name in sys.argv[1:]:
            if not os.path.exists(file_name):
                print(f'{file_name} not in current working directory')
            else:
                unig, big = unigram_bigram_dict(file_name)
                pickle.dump(unig, open(f'{file_name}.unigrams.p', 'wb'))
                pickle.dump(big, open(f'{file_name}.bigrams.p', 'wb'))





if __name__ == "__main__":
    main()
