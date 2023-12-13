import re
from itertools import combinations

class Text_Analysis:
    def __init__(self, text):
        self.txt = text 
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.candidate_key = self.generate_key_candidate()

    def generate_key_candidate(self):
        # Removes: punctuations, numbers, and \ns 
        cleaned_text = re.sub('[^a-zA-Z]+', ' ', self.txt) 
        letterCount = {letter: 0 for letter in self.alphabet}
        
        for letter in cleaned_text:
            if letter in self.alphabet:
                letterCount[letter] += 1
        
        sorted_items = sorted(letterCount.items(), key=lambda x: x[1], reverse=True)
        # Extract the keys as strings
        return [str(key) for key, _ in sorted_items]
    
    @staticmethod
    def key_application(txt, key, plain_text_key):
        trial_text = txt.translate(str.maketrans(key, plain_text_key))
        trial_text = trial_text.replace('\n', ' ')
        return trial_text
    
    @staticmethod
    def key_permutations(s):
        for i,j in combinations(range(len(s)), 2): #couples of position
            res = list(s)
            res[i], res[j] = res[j], res[i]
            yield ''.join(res)

    
    

    
    
    
    

    


    


        
    



