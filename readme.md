# Lexicon machine

The lexicon machine is stored in the file **lexikonautomat.py**. The state class is located in the file **state.py**.

## main program

### Start of the program

The main program is stored in the file **main.py**. The program can be started without command line arguments.
After calling the program, the user has the option of either loading the lexicon automaton from a saved file (using the "load" option) or constructing it from a word list (using the "wordlist" option). If the user selects the option to load the lexicon automaton from a word list, he is asked to enter a text file from which the word list is to be read.

The text file with the word list consists of words that are line by line (separated by newlines).

*possible error messages*:

* If there is no saved machine, the user will be informed and asked to initialize the machine with the help of a word list.

* If the text file does not exist, a FileNotFound Error is returned and the user is informed that the file from which the word list should be loaded could not be found. The program ends automatically and must be restarted.

### Main menu

After the lexicon machine has been constructed, the main menu of the program is called up.
There are several options in the main menu that can be selected. The numbers behind the respective options indicate the input.
After entering an option, the main menu appears again and the user can enter further options.

* Option 1 stands for the word query: Here the user can query any number of words, whereupon the program returns whether the word entered is in the lexicon machine or not. The word query is ended by entering the empty word.

* with option 2 the lexicon automaton is drawn.

* With option 3, the user can have the language of the lexicon machine displayed.

* With the option q or quit the user can exit the main menu.

* If an invalid option is entered, the user is made aware of this and asked to enter a valid option.

**Implemented extensions**:

* graphic representation
* Language of the encyclopedia
* Save and load
