![Alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Skytale.png/640px-Skytale.png)

# Text Decryption Project

This project implements a text decryption algorithm using a brute-force approach with multiprocessing in Python. The goal is to decrypt a given ciphertext by trying different keys and scoring the results based on a specified scoring function.

## Score function 
\begin{equation}
\text{{key\_score}} = \sum_{k, v \in \text{{self.n\_grams}}} \left( v \cdot \log(\text{{plain\_text\_n\_grams}}[k]) \right)
\end{equation}

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
