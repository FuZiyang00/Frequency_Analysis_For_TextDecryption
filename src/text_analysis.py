import re
from itertools import combinations


class Text_Analysis:
    def __init__(self, text):
        self.txt = text 
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.frequency_dict = self.dictionary()
    
    def dictionary(self):
        cleaned_text = re.sub('[^a-zA-Z]+', ' ', self.txt) 
        letterCount = {letter: 0 for letter in self.alphabet}
        
        for letter in cleaned_text:
            if letter in self.alphabet:
                letterCount[letter] += 1
        
        return letterCount

    def generate_key_candidate(self, corpus_freq):
        # Removes: punctuations, numbers, and \ns 
        sorted_txt_freq = dict(sorted(self.frequency_dict.items(), key=lambda x: x[1], reverse=True))
        sorted_corpus_freq = dict(sorted(corpus_freq.items(), key=lambda x: x[1], reverse=True))
        merged_dict = {key1: key2 for key1, key2 in zip(sorted_txt_freq, sorted_corpus_freq)}
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
        # Convert key and plain_text_key to strings
        key = str(cipher_key)
        
        # Apply translation
        trial_text = txt.translate(str.maketrans(key, alphabet))
        trial_text = trial_text.replace('\n', ' ')
        return trial_text

    
    

    
    
    
    

    


    


        
    



