from preprocess import *
from random import shuffle, randint

def main_program():
    print('Welcome to your flashcard session!')
    print('----------------------------------------')
    while True:
        filename = input('Enter your flashcard file name: ')
        print('Loading flashcards ... ')
        try:
            entries, tags = process_file(filename)
            break
        except:
            print('Loading failed. Try another filename?')
    print('Loading successful!')
    print('Tag list: ')
    for tag in tags:
        print('\t', tag)
    print('----------------------------------------')
    tagflag = True

    while True:
        temp = input('Enter your tag mode (ALL or ANY): ')
        if temp.lower() == 'all': break
        if temp.lower() == 'any': 
            tagflag = False
            break
        print('Invalid reply! Please try again ...')

    while True: # chose_tag-is-empty loop
        while True:
            temp = input('Enter your chosen tags (comma seperated): ')
            chosen_tags = [t.strip() for t in temp.split(',')]
            if chosen_tags != []: break
        
        print('Chosen tag list: ')
        for tag in chosen_tags:
            print('\t', tag)

        print('Picking tagged words ...')
        chosen_entries = []
        if tagflag == True:
            for entry in entries:
                include = True
                for tag in chosen_tags:
                    if tag not in entry[-1]:
                        include = False
                        break
                if include: chosen_entries.append(entry)
        else:
            for entry in entries:
                include = False
                for tag in chosen_tags:
                    if tag in entry[-1]:
                        include = True
                        break
                if include: chosen_entries.append(entry)

        if chosen_entries != []: break
        else: print('No words was chosen. Try again?')

    print('Word list picked! Shuffling ...', end='')
    shuffle(chosen_entries)
    print('Done! ')
    input('Press ENTER to start')
    print()
    while chosen_entries:
        ind = randint(0, len(chosen_entries)-1)
        word, meaning, _ = chosen_entries[ind]
        input('Entry: '+word)
        if len(meaning) > 1:
            print('Explanation:')
            for i, m in enumerate(meaning):
                print(f'\t{i+1}. {m}')
        elif len(meaning) == 1:
            print('Explanation: ', meaning[0])
        else:
            print('Explanation: - ')
        print()
        temp = input('Put back to list?')
        if temp.lower() in ['', 'n', 'no']:
            chosen_entries.pop(ind)
        print()
    print('That the all list done!')
    print('Piece')


if __name__ == '__main__':
    main_program()