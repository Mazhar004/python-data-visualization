import enchant

import pickle
import os

json_dictionary_root = os.path.split(os.path.abspath(__file__))[0]


class Dictionary():
    '''
    Dictionary data collected from Oxford dictionary text file & json file from https://github.com/HarikaGurram/DictionaryEnglishTransfer
    All English word & meaning comprise in a JSON file

    Total number of available word is 131k(1,31,965)
    '''
    file_name = json_dictionary_root + '/Dictionary/dictionary.pickle'
    advanced_dict = enchant.Dict("en_US")

    def __init__(self):
        self.dictionary = self.dataload()

    def dataload(self):
        with open(Dictionary.file_name, 'rb') as fh:
            return pickle.load(fh)

    def keys(self):
        return self.dictionary.keys()

    def values(self):
        return self.dictionary.values()

    def items(self):
        return self.dictionary.items()

    def suggest(self, key):
        return Dictionary.advanced_dict.suggest(key)

    def __getitem__(self, key):
        try:
            return self.dictionary[key.upper()]
        except:
            print(
                "We didn't find {}.\nPlease have a look similar word matching with your input key".format(key))
            return self.suggest(key.capitalize())
