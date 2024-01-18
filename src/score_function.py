import re, operator
import math 

class Score_Function:
    def __init__(self, txt):
        self.txt = txt
        self.n_grams = self.n_grams_dictionary()

    @staticmethod
    def letterNGrams(msg, n):
        return [msg[i:i+n] for i in range(len(msg) - (n-1))] 
        # returns a lsit of the ngrams of a given word: hello, 2 = [he, el, ll, lo]

    
    def n_grams_dictionary(self):
        txt_words = re.findall(r"[\w']+", self.txt) # returns a list of words found in the string
        bigrams = {}
        for i in txt_words:
            for element in Score_Function.letterNGrams(i,2):
                if element not in bigrams:
                    bigrams[element] = 1
                else:
                    bigrams[element]+=1

        return dict(sorted(bigrams.items(), key=operator.itemgetter(1),reverse=True))
    
    def get_key_score(self, plain_text_n_grams):
        key_score=0
        for k,v in self.n_grams.items():
            if k in plain_text_n_grams:
                key_score = key_score + v*math.log(plain_text_n_grams[k])
                # v = the frequency of the n-gram in the encrypted text 
                # k = frequency of the same n-gram in a plain text
                # use of log = frequently appearing ngram --> positive number 
                # use of log = rarely appearing ngram --> negative number
       
        return key_score