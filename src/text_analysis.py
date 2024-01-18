import re
from itertools import combinations


class Text_Analysis:
    def __init__(self, text):
        self.txt = text 
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.frequency_dict = self.dictionary()
    
    def dictionary(self):
        # dictionary containing the encrypted text letters frequency
        cleaned_text = re.sub('[^a-zA-Z]+', ' ', self.txt) 
        letterCount = {letter: 0 for letter in self.alphabet}
        
        for letter in cleaned_text:
            if letter in self.alphabet:
                letterCount[letter] += 1
        
        return letterCount

    def generate_key_candidate(self, corpus_freq):
        # Step 1: Sort the frequency dictionaries in descending order based on values
        sorted_txt_freq = dict(sorted(self.frequency_dict.items(), key=lambda x: x[1], reverse=True))
        sorted_corpus_freq = dict(sorted(corpus_freq.items(), key=lambda x: x[1], reverse=True))

        # Step2: map the letters based on their frequency: {[encrypted_letter]: corpus_letter}
        merged_dict = {key1: key2 for key1, key2 in zip(sorted_txt_freq, sorted_corpus_freq)}
        
        # sort the dictionary by alphabetical order
        sorted_merge_dict = dict(sorted(merged_dict.items(), key=lambda x: x[1], reverse=False))
        
        # Extract the keys as strings
        return ''.join(key for key in sorted_merge_dict)
    
    @staticmethod
    def key_permutations(s):
        for i,j in combinations(range(len(s)), 2): #couples of position
            res = list(s)
            res[i], res[j] = res[j], res[i]
            yield ''.join(res)
    
    @staticmethod
    def key_application(txt, cipher_key, alphabet):
        key = str(cipher_key)
        
        # Apply the decryption key on the encrypted text
        trial_text = txt.translate(str.maketrans(key, alphabet))
        trial_text = trial_text.replace('\n', ' ')
        return trial_text

    
    

    
    
    
    

    


    


        
    



