from src.decryption import decryption
from src.text_analysis import Text_Analysis

if __name__ == "__main__": 
    
    # Files reading 
    c = open('ciphertext.txt','r',encoding='utf-8')
    ciphertext = c.read() 
    
    p = open('corpus-war-and-peace-anna-karienina.txt','r',encoding='utf-8')
    corpus = p.read()
    corpus = corpus.lower()
    corpus_ = Text_Analysis(corpus)
    plain_key = corpus_.candidate_key

    decryption_key = decryption.brute_forcing(ciphertext[:500], corpus, 10)
    descrypted_text = Text_Analysis.key_application(ciphertext, decryption_key, plain_key)
