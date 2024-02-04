![Alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Skytale.png/640px-Skytale.png)

# Text Decryption Project

This project implements a text decryption algorithm using a brute-force approach with multiprocessing in Python. The goal is to decrypt a given ciphertext by trying different keys and scoring the results based on a specified scoring function.

## Score function 

The key score is calculated using the following formula:

$$ \text{key score} = \sum_{k \in E \cap D} F(k) \cdot \log(\text{plain text n grams}[k]) $$

where:

- \( E \) is the set of n-grams in the encrypted text,
- \( D \) is the set of n-grams in the decrypted (plain) text,
- \( F(k) \) is the frequency of n-gram \( k \) in the encrypted text,
- \( \cap \) represents the intersection of sets,
- \( \text{plain\_text\_n\_grams}[k] \) represents the frequency of n-gram \( k \) in the decrypted text,
- \( \log \) is the natural logarithm.


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
