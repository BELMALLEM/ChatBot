# ChatBot :relaxed:
This ChatBot is a basic program built in python and have the ability to interact with the user using programmed questions and responses.
Its ability is in understanding the inputs by looking for known patterns.

# Installation

1. Download the folder
2. Open it in a Shell command
3. Tap:
 > Python execute.py
4. Play the game with your **Bot** 

# Abilities
 * Easy to develop and add more functionalities
 * It can send Emails automatically just by saying it.
 * Can get the latest news for you using `myallies-breaking-news` *API*
 * Can search in Wikipedia by taping questions like `What does mean ... ?`
 
 # Used libraries
 This project is based on three principal libraries:
   * 'tflearn.py': TFlearn is a modular and transparent deep learning library built on top of Tensorflow.
   * 'numpy.py': NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
   * 'json.py':

#  Architecture
* `Actions.py`: Contains methods for actions like sending mails, looking for news...
   It can be updated to do any task you want by adding a method you created and linking it the main file.
* `Execute.py`: The main file of executions.
* `Intents.json`: The dictionnary of the Bot that contains the programmed questions, answers and an actions to do.
* `Training.py`: After each update on `intents.json` the bot should create patterns of the dictionnary, so this file should be executed after updating in the intents.
>{

>    "tag": "searchme",
    
>    "patterns": ["who is that ?", "where is that ?"],

>    "responses": [""],

>    "action": "search"

>}
* `TextProcess.py`: Some essential functions for text processing that the bot use.

# What to do next ?
This bot can be adopted to every project and easily updated, so feel free to add as much of functionalities you want.

>The artist must bow to the monster of his own imagination  - Richard Wright
