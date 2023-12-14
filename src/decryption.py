from .score_function import Score_Function
from .text_analysis import Text_Analysis


class Text_decryption:
    @staticmethod
    def brute_forcing(txt, plain_text, attempts):
        cipher_txt = Text_Analysis(txt)
        corpus = Text_Analysis(plain_text)

        # get the letters frequency of the corpus 
        corpus_freq = corpus.frequency_dict
        alphabet = corpus.alphabet 

        # retrieve the first candidate decryption key 
        best_key = cipher_txt.generate_key_candidate(corpus_freq)
        print("fist key: {}".format(best_key))
        # decrypt the text 
        best_trial = Text_Analysis.key_application_parallel(txt, best_key, alphabet)

        # compute the score of this trial 
        trial = Score_Function(best_trial)
        plain = Score_Function(plain_text)
        plain_text_n_grams = plain.n_grams
        best_score = trial.get_key_score(plain_text_n_grams)

        for i in range(attempts):
            print("Attempt number {}".format(i))
            keys = list(Text_Analysis.key_permutations(best_key))
            
            # iterarate over the permutations of the first retrieved key 
            for key in keys:
                new_trial = Text_Analysis.key_application_parallel(txt, key, alphabet)
                trial = Score_Function(new_trial)
                score = trial.get_key_score(plain_text_n_grams)

                if score > best_score:
                    best_score = score 
                    best_key = key
                    print("newly found best decryption key: {}".format(best_key))
                    break
        
        return best_key
            

