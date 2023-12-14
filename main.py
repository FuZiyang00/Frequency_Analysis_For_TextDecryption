from src.decryption import Text_decryption
from src.text_analysis import Text_Analysis

if __name__ == "__main__": 
    
    # Files reading 
    c = open('ciphertext.txt','r',encoding='utf-8')
    ciphertext = c.read() 
    
    p = open('corpus-war-and-peace-anna-karienina.txt','r',encoding='utf-8')
    corpus = p.read()
    corpus = corpus.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decryption_key = Text_decryption.brute_forcing(ciphertext, corpus, 10)
    best_trial = Text_Analysis.key_application(ciphertext, decryption_key, alphabet)

    with open('best_trial.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(best_trial)


    
