from itertools import permutations as pm
from dictionary import Dictionary


class WordGame():
    '''
    Word generator game with follwing features:
        1. Generate all possible word from a given list of word set
        2. Generate word of given length from a given list of word set
        3. Excess meaning of generated word

    Example:
        from word_game import WordGame
        word_list = ['hard','ware']
        wg = WordGame(word_list)
        print('Word with 6 length',wg.word_gen(6))
        print('Word with 8 length',wg.word_gen(8))
        print('All Generated WordList',wg.all_word)
        print('Word Meaning',wg['Hardware'])

        Output:
        Word with 6 length ['harder', 'redraw', 'warder', 'drawer', 'reward'])
        Word with 8 length ['hardware'])
        All Generated WordList {8: ['hardware'], 6: ['harder', 'redraw', 'warder', 'drawer', 'reward']})
        Word Meaning Defn: Ware made of metal, as cutlery, kitchen utensils, and the like;
                           ironmongery.
    '''
    dictionary = Dictionary()

    def __init__(self, alphabet):
        '''
        alphabet = A list of word
        '''
        self.alphabet = ''.join(i.lower() for i in alphabet)
        self.all_word = {}
        self.words = []

    def word_verify(self, string):
        '''
        Verify string exist or not in dictionary data
        '''
        return bool(WordGame.dictionary[string])

    def word_permu(self, length, accepted_word):
        '''
        Generate all possible word using Permutation
        '''
        for j in set(pm(self.alphabet, length)):
            word = ''.join(j)
            if self.word_verify(word):
                accepted_word.append(word)
        return accepted_word

    def word_gen(self, *args):
        '''
        Generate all words & filter english words
        *args = Enter desired length for generated word(It must be grater than 0 & less than sum of total input word length)
                Default value set to sum of total input word length
        '''
        if len(args) == 0:
            length = len(self.alphabet)
        else:
            length = args[0]
        self.all_word[length] = []
        if length > 0:
            self.all_word[length] = self.word_permu(
                length, self.all_word[length])
        self.words = self.all_word[length]
        return self.all_word[length]

    def __getitem__(self, word):
        '''
        Return meaning of the given word
        '''
        return WordGame.dictionary[word]
