import os
import argparse

import re
import pickle
import json

text_dictionary_root = os.path.split(os.path.abspath(__file__))[0]


class DictionaryForm():
    '''
    Extract data from oxford dictionary text file
    Extract data from json file from https://github.com/HarikaGurram/DictionaryEnglishTransfer
    Store it in a binary format pickle file

    Example:
    dictionary = DictionaryForm(True)
    '''
    data_file1 = text_dictionary_root+'/oxford_dictionary.txt'
    data_file2 = text_dictionary_root + '/english_dictionary.txt'
    pickle_file = text_dictionary_root+'/dictionary.pickle'

    def __init__(self, save_val=False):
        '''
        save_val = For saving json object as pickle data
        '''
        self.oxford_raw = self.read_file(DictionaryForm.data_file1)
        self.ox_split_data = self.json_data_form()
        self.final_dict = self.process_dictionary()
        if save_val:
            self.save(DictionaryForm.pickle_file)

    def read_file(self, filename):
        '''
        Read dictionary text file 
        '''

        with open(filename, 'r') as fh:
            data = ''.join(fh.readlines())
        return data

    def json_data_form(self):
        '''
        Extract word list from text file 
        '''
        ox_split_data = {}
        temp_key = []
        for i in self.oxford_raw.split('\n'):
            if i.isupper():
                temp_key = re.findall(r'[A-Z\-\+\.\s]+', i)[0].strip()
                ox_split_data[temp_key] = []
            else:
                try:
                    ox_split_data[temp_key].append(i)
                except:
                    pass
        return ox_split_data

    def meaning_process(self, str_list):
        '''
        Extract word meaning from text file 
        '''
        result = []
        str_list = ('\n'.join(str_list)).split('\n\n')
        for i in str_list:
            result.append(i)
        return '\n'.join(result[1:]).strip()

    def process_dictionary(self):
        '''
        Extract data as json format from text file 
        '''
        final_dict = {}
        for i, j in self.ox_split_data.items():
            final_dict[i] = self.meaning_process(j)

        file2_data = self.read_file(DictionaryForm.data_file2)
        file2_json_data = json.loads(file2_data)
        for i, j in file2_json_data.items():
            final_dict[i.upper()] = '\n'.join(j)
        return final_dict

    def save(self, filename):
        '''
        Save json dictionary data as binary pickle file 
        '''
        try:
            with open(filename, 'wb') as fh:
                pickle.dump(self.final_dict, fh)
            print('Successfully saved the JSON data.')
        except Exception as Err:
            print('Save status unsuccessful.Details can be found below:')
            print("Error due to {}".format(Err))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", default=True, type=bool,
                        required=False, help="Save json file True/False")

    args = parser.parse_args()
    dictionary = DictionaryForm(args.save)
