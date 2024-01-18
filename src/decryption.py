from multiprocessing import Process, Manager
from .score_function import Score_Function
from .text_analysis import Text_Analysis

class Text_decryption:

    @staticmethod
    def process_keys(keys_subset, txt, alphabet, plain_text_n_grams, result_queue, original_score):
        try:
            for key in keys_subset:
                new_trial = Text_Analysis.key_application(txt, key, alphabet) # applying the candidate key 
                trial = Score_Function(new_trial)
                score = trial.get_key_score(plain_text_n_grams)

                if score > original_score:
                    result_queue.put((key, score))
        except Exception as e:
            print(f"Error in process_keys: {e}")

    @staticmethod
    #wrapper method for process_keys
    def brute_force_worker(keys_subset, txt, alphabet, plain_text_n_grams, result_queue, original_score):
        Text_decryption.process_keys(keys_subset, txt, alphabet, plain_text_n_grams, result_queue, original_score)

    @staticmethod
    def brute_forcing(txt, plain_text, attempts, num_cores=4):
        cipher_txt = Text_Analysis(txt)
        corpus = Text_Analysis(plain_text)

        # get the letters frequency of the plain text
        corpus_freq = corpus.frequency_dict
        alphabet = corpus.alphabet

        # retrieve the first candidate decryption key
        best_key = cipher_txt.generate_key_candidate(corpus_freq)
        print("first key: {}".format(best_key))

        # decrypt the text
        best_trial = Text_Analysis.key_application(txt, best_key, alphabet)

        # compute the score of this trial
        trial = Score_Function(best_trial) 
        plain = Score_Function(plain_text) 
        plain_text_n_grams = plain.n_grams # ngrams dictionary of the plain text
        best_score = trial.get_key_score(plain_text_n_grams)

        with Manager() as manager: # helps in coordinating and synchronizing access to shared resources
            result_queue = manager.Queue() # shared queue used for communication between processes
            # As each process discovers a better key, it puts the key and its corresponding score into the queue

            for i in range(attempts):
                print("Attempt number {}".format(i))
                keys = list(Text_Analysis.key_permutations(best_key))
                chunk_size = len(keys) // num_cores

                # Create sublists using list comprehension
                key_chunks = [keys[i:i + chunk_size] for i in range(0, len(keys), chunk_size)]

                processes = []
                for j in range(num_cores):
                    process = Process(target=Text_decryption.brute_force_worker,
                                      args=(key_chunks[j], txt, alphabet, plain_text_n_grams,
                                            result_queue, best_score))
                    # target argument specifies the function to be executed in the new process 

                    processes.append(process) 
                    # keeps track of all the processes that have been created. 
                    # This list is later used when waiting for each process to finish using .join()
                    
                    process.start()  # called to initiate the execution of each process

                # ensures that the main program doesn't proceed until all parallel processes have completed their tasks
                for process in processes:
                    process.join() 

                # Check if any process found a better key
                found_better_key = False
                while not result_queue.empty():
                    key, score = result_queue.get()
                    if score > best_score:
                        best_key = key
                        best_score = score
                        print("newly found best key: {}".format(best_key))
                        found_better_key = True
                        break
                
                if not found_better_key:
                    break  # Break from the outer loop if no better key is found

        return best_key

