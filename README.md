# ChatBot :robot:
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

#  Architecture
* `Actions.py`: Contains methods for actions like sending mails, looking for news...
   It can be updated to do any task you want by adding a method you created and linking it the main file.
* `Execute.py`: The main file of executions.
* `Intents.json`: The dictionnary of the Bot that contains the programmed questions, answers and an actions to do.
* `Training.py`: After each update on `intents.json` the bot should create pattern to memorise them.
>{
    "tag": "searchme",
    "patterns": ["who is that ?", "where is that ?", "when  the thing had happened ?", "what is that ?", "what does mean that ?",
    "do you know somthing about that ?", "i want to know about that"],
    "responses": [""],
    "action": "search"
 }
* `TextProcess.py`: Some essential functions for text processing that the bot use.
