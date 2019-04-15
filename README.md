# <center>ELEN4020A Lab 3 Exercises </center>
-
###### Tyson Cross       1239448
###### Michael Nortje    1389486
###### Josh Isserow      675720

Lab 3 exercises were written in Python 3.7.2 <br> <br>
The code requires [mrjob v0.6.7](https://pythonhosted.org/mrjob/) to be installed. A requirements.txt file is provided for convenience. 

### Setup ###
Create and then source a virtual environment, then install the dependencies in the environment:

            $ python -m venv /path/to/new/virtual/environment
            $ source </path/to/new/virtual/environment>/bin/activate
            $ pip install -r requirements.txt
            
### Instructions ###
Return all the words in a text, with the total word counts:

            $ python WordCount.py <INPUT_TEXT_FILE> -q [--stop-word STOP_WORDS_FILE]
            
Return the top K frequencies of word occurance:

            $ python WordFreq.py <INPUT_TEXT_FILE> -q [--stop-word STOP_WORDS_FILE] [--limit K]
            
Return an inverse index of the first K lines of text by word and the line index they occur on:

            $ python WordInverseIndex.py <INPUT_TEXT_FILE> -q [--stop-word STOP_WORDS_FILE] [--limit K] [--index-limit L]
