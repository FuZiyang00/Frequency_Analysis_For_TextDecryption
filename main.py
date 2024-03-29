from src.decryption import Text_decryption
from src.text_analysis import Text_Analysis
import time
import sys

if __name__ == "__main__": 

    if len(sys.argv) != 3:
        print("Usage: python main.py ciphertext_file corpus_file")
        sys.exit(1)

    ciphertext_filename = sys.argv[1]
    corpus_filename = sys.argv[2]
    
    # Files reading
    with open(ciphertext_filename, 'r', encoding='utf-8') as c:
        ciphertext = c.read()

    with open(corpus_filename, 'r', encoding='utf-8') as p:
        corpus = p.read()
        corpus = corpus.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    start_time_key_app = time.time()
    decryption_key = Text_decryption.brute_forcing(ciphertext, corpus, 20)
    best_trial = Text_Analysis.key_application(ciphertext, decryption_key, alphabet)
    end_time_key_app = time.time()
    key_app_duration = end_time_key_app - start_time_key_app
    key_app_minutes, key_app_seconds = divmod(int(key_app_duration), 60)
    print("best discovered key: {}". format(decryption_key))
    print(f"Key application execution time: {key_app_minutes} minutes and {key_app_seconds} seconds")

    with open('best_trial.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(best_trial)


    
