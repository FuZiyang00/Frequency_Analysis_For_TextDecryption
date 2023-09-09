import pandas as pd 
from functions import Text_Analysis, decryption
import logging
if __name__ == "__main__": 
    
    # Texts reading
    f = open('ciphertext.txt','r',encoding='utf-8')
    ciphertext = f.read() 
    
    f = open('corpus-war-and-peace-anna-karienina.txt','r',encoding='utf-8')
    corpus = f.read()
    corpus = corpus.lower()
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Letters Frequency Analysis
    cleaned_corpus = Text_Analysis.text_cleaning(corpus) # removal of all the numbers and special characters
    cleaned_ciphertext = Text_Analysis.text_cleaning(ciphertext)

    corpus_distribution = Text_Analysis.getLetterCount(cleaned_corpus, alphabet) # Letters frequency of a large English Corpus 
    corpus_df = pd.DataFrame([corpus_distribution]).transpose()
    corpus_df=corpus_df.reset_index()
    corpus_df.rename(columns={0: 'corpus_frequency','index':'corpus_letters'}, inplace=True)

    cipher_distribution = Text_Analysis.getLetterCount(cleaned_ciphertext, alphabet) # Letters frequency of the ciphertext 
    cipher_df = pd.DataFrame([cipher_distribution]).transpose()
    cipher_df=cipher_df.reset_index()
    cipher_df.rename(columns={0: 'cipher_frequency','index':'cipher_letters'}, inplace=True)

    sort_cipher_df = cipher_df.sort_values(by=['cipher_frequency'], ascending=False).reset_index().drop(columns='index') 
    sort_corpus_df = corpus_df.sort_values(by=['corpus_frequency'], ascending=False).reset_index().drop(columns='index')
    compare_df = sort_corpus_df.join(sort_cipher_df['cipher_letters']).join(sort_cipher_df['cipher_frequency'])
    compare_df = compare_df.sort_values('corpus_letters')
    compare_df = compare_df.reset_index().drop(columns='index') # Comparison table between the 2 distributions 
    print(compare_df)

    # Get the first decryption key from the antecedent analysis 
    first_key = decryption.frequency_key(compare_df)
    print("The first candidate key: {}".format(first_key))
     
    # Applying the key to the ciphertext 
    manual_attempt = decryption.key_application(ciphertext, first_key, alphabet)
    print(manual_attempt[:500])

    # Manually swapping the 'wrong letters' 
    manual_attempt = manual_attempt.replace('y', 'P')
    manual_attempt = manual_attempt.replace('p', 'Y')
    manual_attempt = manual_attempt.replace('h','I')
    manual_attempt = manual_attempt.replace('i', 'N')
    manual_attempt = manual_attempt.replace('n', 'H')
    manual_attempt = manual_attempt.replace('k', 'V')
    manual_attempt = manual_attempt.replace('v', 'K')
    print(manual_attempt[:500].upper())


