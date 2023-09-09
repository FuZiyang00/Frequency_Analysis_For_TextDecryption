# Frequency Analysis For TextDecryption
The goal of this project is to make use of letters frequency analysis to decrypt a cipher text, in which the letters have been swapped. 
Two approaches are used:
## Manual Decryption 
in which we start from an initial candidate decryption key and subsequently we manually swapped the letters to adjust the word; 
## Authomatic Decryption 
in which we start from the same inital candidate decryption key and give to the script a finite number of trial to adjust the initial key in order to have a more precise decrypted text. 
We needed to implement a scoring system to evaluate how good the decryption is, based on the bigram frequency:
Logarithm method S = (obs.freq*log(exp.freq))