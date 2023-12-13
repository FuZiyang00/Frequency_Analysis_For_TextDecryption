import re, operator
from itertools import combinations
import math, string 

class Text_Analysis: 
    @staticmethod
    def text_cleaning (txt):
        cleaned_text = re.sub('[^a-zA-Z]+', ' ', txt) #removes: punctuations, numbers and \ns 
        return cleaned_text
    
    @staticmethod
    def getLetterCount(message, alphabet):
        letterCount = {letter: 0 for letter in string.ascii_lowercase} 
        for letter in message:
            if letter in alphabet:
                letterCount[letter] += 1
        return letterCount

class decryption: 
    @staticmethod
    def frequency_key (df):
        key = ''
        for i in df['cipher_letters']:
            key = key+i
        return key
    
    @staticmethod
    def key_application (msg, key, alphabet):
        msg = msg.translate(str.maketrans(key, alphabet))
        msg = msg.replace('\n'," ")
        return msg
    
    @staticmethod
    def letterNGrams(msg, n):
        return [msg[i:i+n] for i in range(len(msg) - (n-1))]
    
    @staticmethod
    def score_text_bigram(txt):
        txt_words = re.findall(r"[\w']+", txt)
        bigrams = {}
        for i in txt_words:
            for element in decryption.letterNGrams(i,3):
                if element not in bigrams:
                    bigrams[element] = 1
                else:
                    bigrams[element]+=1
        
        sorted_bigrams = dict(sorted(bigrams.items(), key=operator.itemgetter(1),reverse=True))
        return sorted_bigrams
    
    @staticmethod
    def key_permutations(s):
        for i,j in combinations(range(len(s)), 2): #couples of position
            res = list(s)
            res[i], res[j] = res[j], res[i]
            yield ''.join(res)
    
    @staticmethod
    def get_key_score(txt,scoring_parameter):
        score_trial= decryption.score_text_bigram(txt)
        cipher_score=0
        for k,v in score_trial.items():
            if k in scoring_parameter:
                cipher_score = cipher_score + v*math.log(scoring_parameter[k])
        return cipher_score
    
    @staticmethod
    def brute_forcing (ciphertext, initial_key, alphabet, scoring_parameter, attempts):
        candidate_plaintext= decryption.key_application(ciphertext, initial_key, alphabet) 
        max_score= decryption.get_key_score(candidate_plaintext,scoring_parameter)
        best_key=initial_key
        permutations= len(best_key)*(len(best_key)-1) #numbers of permutations, up To 2 Letter Changes per permutation, of the frequency key

        for i in range(attempts):
            print("iteration", i)
            p=list(decryption.key_permutations(best_key))                                  
            
            best_candidate=candidate_plaintext
            perc=[10,20,30,40,50,60,70,80,90]

            for idx, k in enumerate(p):

                advance=int(100*idx/permutations)
                if advance in perc:
                    print(f'computed ',advance, '% of the permutations')
                    perc.pop(0)
                
                candidate_plaintext = decryption.key_application(ciphertext, k, alphabet)
                score= decryption.get_key_score(candidate_plaintext,scoring_parameter)
                
                if score>max_score:
                    max_score=score
                    best_key=k
                    best_candidate=candidate_plaintext
                    print('new best key:', best_key)
                    break
        
        return best_key, best_candidate

