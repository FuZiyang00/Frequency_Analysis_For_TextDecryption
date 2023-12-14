from .score_function import Score_Function
from .text_analysis import Text_Analysis
import multiprocessing


class Text_decryption:

    @staticmethod
    def process_keys(keys_subset, txt, alphabet, plain_text_n_grams, result_queue, stop_flag, original_score):

        for key in keys_subset:
            new_trial = Text_Analysis.key_application(txt, key, alphabet)
            trial = Score_Function(new_trial)
            score = trial.get_key_score(plain_text_n_grams)

            if score > original_score:
                result_queue.put((key, score))
                stop_flag.value = 1  # Set the stop flag to signal termination
                break 


    @staticmethod
    def brute_forcing(txt, plain_text, attempts, num_cores = 4):
        cipher_txt = Text_Analysis(txt)
        corpus = Text_Analysis(plain_text)

        # get the letters frequency of the corpus 
        corpus_freq = corpus.frequency_dict
        alphabet = corpus.alphabet 

        # retrieve the first candidate decryption key 
        best_key = cipher_txt.generate_key_candidate(corpus_freq)
        print("fist key: {}".format(best_key))
        # decrypt the text 
        best_trial = Text_Analysis.key_application(txt, best_key, alphabet)

        # compute the score of this trial 
        trial = Score_Function(best_trial)
        plain = Score_Function(plain_text)
        plain_text_n_grams = plain.n_grams
        best_score = trial.get_key_score(plain_text_n_grams)

        for i in range(attempts):
            found_better_key = False
            print("Attempt number {}".format(i))
            keys = list(Text_Analysis.key_permutations(best_key))
            chunk_size = len(keys) // num_cores
            # Create sublists using list comprehension
            key_chunks = [keys[i:i + chunk_size] for i in range(0, len(keys), chunk_size)]

            result_queue = multiprocessing.Queue()
            stop_flag = multiprocessing.Value('i', 0)  # Shared flag to signal termination

            processes = []
            for j in range(num_cores):
                process = multiprocessing.Process(target=Text_decryption.process_keys, 
                                                  args=(key_chunks[j], txt, alphabet, plain_text_n_grams, 
                                                        result_queue, stop_flag, best_score))
                processes.append(process)
                process.start()

            # Wait for any process to find a better key or finish
            for process in processes:
                process.join()

                # Check if any process found a better key and terminate others
                if stop_flag.value == 1:
                    for process in processes:
                        process.terminate()
                    found_better_key = True
                    break  # Break from the loop if a better key is found
            
            key, score = result_queue.get()
            best_key = key
            best_score = score
            print("newly found best key: {}". format(best_key))

            if not found_better_key:
                break # Break from the outer loop if no better key is found
        
        return best_key
            

