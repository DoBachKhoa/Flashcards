# Flashcards

A terminal app to help study flashcards.

## Requirements

Python3. If needed to, install ```python-docx``` with the command ```pip install python-docx```, and you are good.

## Create you flashcard collections

At the start of the program, you will be asked to enter the file name of the collection. You can create a collection by simply write the word lists in a docx file (using Microsoft Word for example), and entering the relative directory of that file.

The format is ```Word \tab Explanation 1 | Explanation 2 | ... | Tags(comma seperated) \n```. Each paragraph (meaning each endline) represents an entry. Using docx gives the convenience of adjusting the page and tab alignments so that the file itself is easy to read and is useful to you.

Just in case, please don't make a huge (like 1000+ words long) file, but divide them out: I am not sure how much it takes for memory to be an issue, and Python's handling string could not be done at the speed of light.

## Use the program

Use the command ```python3 program.py```.
The program will ask for your file name, then the tag mode, and finally your tags. Enter the tags of the words that you want to select for revision. Enter ```all``` if you want only the words with all the chosen tags, and '''any''' for the words having any of the selected one.

Press ENTER to start (when asked). The program will start feeding entries to you. Press enter to reveal the explanations (meanings, examples, ...). Then write 'y' if you want to recycle the entry, and 'n' if you are good and want to drop it (or just ENTER, it is fine).

## Notes:

- Keep it within utf 8, I doubt it would work otherwise
- Have fun reviewing!