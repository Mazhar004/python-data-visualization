import argparse
from word_game import WordGame

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", type=str,
                        required=True, help="Enter word")
    parser.add_argument("--length", type=int,
                        required=True, help="Enter word")
    args = parser.parse_args()

    wg = WordGame([args.word])
    print('Word with length of {}:\n{}\n'.format(
        args.length, wg.word_gen(args.length)))
    for i in wg.words:
        print('{}\n\n{}\n'.format(i.upper(), wg[i]), end=50*'-'+'\n')
