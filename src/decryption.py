from score_function import Score_Function
from text_analysis import Text_Analysis

class decryption:

    @staticmethod
    def brute_forcing (txt, plain_text, attempts):
        # initialize the text analysis class with the encrypted key 
        cipher_txt = Text_Analysis(txt)
        candidate_key = cipher_txt.candidate_key

        # initialize the text analysis class with the plain text
        corpus = Text_Analysis(plain_text)
        corpus_key = corpus.candidate_key

        # first trial text 
        trial_1 = cipher_txt.key_application(txt, candidate_key, corpus_key)
        
        # get the n-grams dictionary of the plain text 
        plain_score = Score_Function(plain_text)
        plain_n_grams = plain_score.n_grams

        # score of the first trial text 
        init = Score_Function(trial_1)
        init_score = init.get_key_score(plain_n_grams)

        best_key = candidate_key
        best_score = init_score

        # starting to brute force
        for i in range(attempts):
            key_permutations = [Text_Analysis.key_permutations(best_key)]

            for key in key_permutations:
                trial = cipher_txt.key_application(txt, key, corpus_key)
                trial_init = Score_Function(trial)
                trial_score = trial_init.get_key_score(plain_n_grams)

                if trial_score>best_score:
                    best_score=trial_score
                    best_key= key
                    break
            
            print("attempt number {}, new candidate_key: {}".format(i, best_key))
        
        return best_key


