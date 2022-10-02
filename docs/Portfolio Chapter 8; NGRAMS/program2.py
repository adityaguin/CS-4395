'''
Collaborators: Aditya Guin (asg180005), Varin Sikand (vss180000)
Date: 10/02/2022
CS 4395.001
'''
import os.path
import sys
from collections import Counter
from functools import reduce

from nltk import word_tokenize, ngrams
import pickle


def main():
    if len(sys.argv) < 4:
        print('File for text not given in sysarg. Program ending')
    else:
        uni_bi_dict = {}
        test_file_name = sys.argv[1]
        sol_file_name = sys.argv[2]
        for file_name in sys.argv[3:]:
            if not os.path.exists(file_name):
                print(f'{file_name} not in current working directory')
            else:
                unigrams = pickle.load(open(f'{file_name}.unigrams.p', 'rb'))
                bigrams = pickle.load(open(f'{file_name}.bigrams.p', 'rb'))
                uni_bi_dict[file_name] = (unigrams, bigrams)
        total_length = sum(len(uni_dict) for uni_dict, _ in uni_bi_dict.values())
        bigram_prob = lambda bigram, bigrams, unigrams: (bigrams[bigram] + 1) / (unigrams[bigram[0]] + total_length)

        sol_list = []
        with open(os.path.abspath(test_file_name), 'r', encoding='utf8') as f:
            for i, line in enumerate(f):
                curr_max = (0.0, '')
                bigrams = list(ngrams(word_tokenize(line), 2))
                for file_name in sys.argv[3:]:
                    prob_lambda = lambda a, bigram: a * bigram_prob(bigram, uni_bi_dict[file_name][1],
                                                                    uni_bi_dict[file_name][0])
                    prob = reduce(prob_lambda, bigrams, 1) if len(bigrams) > 0 else 0
                    curr_max = max(curr_max, (prob, file_name))

                sol_list.append((i+1, curr_max[1].split('.')[-1]))
        with open('our_solution.txt', 'w', encoding='utf8') as f:
            for thing in sol_list:
                f.write(f'{thing[0]} {thing[1]}\n')
        number_wrong = 0
        with open(os.path.abspath(sol_file_name), 'r', encoding='utf8') as f:
            sol_file_list = [(int(line.split()[0]), line.split()[1]) for line in f]
            for line in sol_file_list:
                if line != sol_list[(line[0]) - 1]:
                    print(f'Line {line[0]} is incorrect')
                    number_wrong += 1

        print(f'Accuracy = {(len(sol_list) - number_wrong) / len(sol_list) * 100.}%')



if __name__ == '__main__':
    main()
