![Alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Skytale.png/640px-Skytale.png)

# Text Decryption Project

This project implements a text decryption algorithm using a brute-force approach with multiprocessing in Python. The goal is to decrypt a given ciphertext by trying different keys and scoring the results based on a specified scoring function.

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
