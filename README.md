![Alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Skytale.png/640px-Skytale.png)

# Text Decryption Project

This project implements a text decryption algorithm using a brute-force approach with multiprocessing in Python. The goal is to decrypt a given ciphertext by trying different keys and scoring the results based on a specified scoring function.

## Score function 

The key score is calculated using the following formula:

$$ \text{key score} = \sum_{k \in E \cap D} F(k) \cdot \log(\text{plain text n grams}[k]) $$

where:

- `E` is the set of n-grams in the encrypted text,
- `D` is the set of n-grams in the plain text,
- `F(k)` is the frequency of the `k-th` n-gram in the encrypted text,
- `plai_text_ngrams[k]` represents the frequency of the `k-th` n-gram in the plain text,
- $E\bigcap D$ represents the intersection of sets


The logarithmic scaling is applied to the frequency of n-grams in the plain text. 

This scaling has a crucial role in highlighting differences in vocabulary usage. When the encrypted text exhibits a vocabulary similar to regular English text, the logarithm of n-gram frequency tends to result in a higher numerical value. Conversely, for highly "irregular" text, the logarithmic term is likely to produce a lower value. 

This logarithmic transformation accentuates distinctions in vocabulary patterns, aiding in the identification of a more accurate decryption key.

## Project Structure
```
project-root/
│
├── src/
│ ├── decryption.py
│ └── score_function.py
│ └── text_analysis.py
|
│── build.sh
├── main.py
└── README.md
```
## Installation 
```
chmod +x build.sh && ./build.sh ciphertext.txt corpus.txt
```
