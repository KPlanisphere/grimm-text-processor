# GrimmTextProcessor

A comprehensive text processing project using Python and NLTK, focused on processing text from Grimms' Fairy Tales. The project involves reading text files, tokenizing the content, removing punctuation, converting text to lowercase, and filtering out stopwords. This project was developed as part of a laboratory exercise to understand the basics of text preprocessing for information retrieval.

## Features

### Overview

The project involves several key tasks:

-   **Tokenization**: Splitting the text into individual words or tokens.
-   **Punctuation Removal**: Removing punctuation marks from the tokens.
-   **Lowercase Conversion**: Converting all text to lowercase.
-   **Stopwords Removal**: Filtering out common words that do not contribute much meaning (e.g., "and", "the").

### Scripts

#### `lab1.1.py`

-   **Read Text File**: Reads content from `lab1.txt`.
-   **Tokenization**: Uses NLTK to tokenize the text.
-   **Remove Punctuation**: Removes punctuation and specific symbols from the text.
-   **Print Output**: Prints the first 100 words after processing.

#### Code Snippet

```python
import re
import string
import nltk
import os

nltk.download('punkt')

# Read the external file content
archivo_path = os.path.join(os.path.dirname(__file__), 'lab1.txt')
with open(archivo_path, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Tokenization using NLTK
palabras = nltk.word_tokenize(texto)

# Split the text into words
palabras = texto.split()

# Print punctuation
print(string.punctuation)

# Define regex to remove punctuation
simbolos_extra = '’'
re_punc = re.compile('[%s%s]' % (re.escape(string.punctuation), re.escape(simbolos_extra)))

# Remove punctuation from each word
stripped = [re_punc.sub('', w) for w in palabras]

# Print the first 100 words
print(stripped[:100])
```

#### `lab1.2.py`

-   **Read Text File**: Reads content from `prueba.txt`.
-   **Tokenization**: Uses NLTK to tokenize the text.
-   **Convert to Lowercase**: Converts all text to lowercase.
-   **Remove Vowels**: Removes vowels from the text.
-   **Print Output**: Prints the first 100 words after processing.

#### Code Snippet

```python
import re
import string
import nltk
import os

nltk.download('punkt')

# Read the external file content
archivo_path = os.path.join(os.path.dirname(__file__), 'prueba.txt')
with open(archivo_path, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Tokenization using NLTK
palabras = nltk.word_tokenize(texto)

# Convert text to lowercase
texto = texto.lower()

# Split the text into words
palabras = texto.split()

# Print punctuation
print(string.punctuation)

# Define regex to remove vowels
simbolos_extra = 'aeiou'
re_punc = re.compile('[%s]' % (re.escape(simbolos_extra)))

# Remove vowels from each word
stripped = [re_punc.sub('', w) for w in palabras]

# Print the first 100 words
print(stripped[:100])
```

#### `lab1.3.py`

-   **Read Text File**: Reads content from `lab1.txt`.
-   **Tokenization**: Uses NLTK to tokenize the text.
-   **Convert to Lowercase**: Converts all text to lowercase.
-   **Remove Punctuation**: Removes punctuation and specific symbols from the text.
-   **Print Output**: Prints the first 100 words after processing.

#### Code Snippet

```python
import re
import string
import nltk
import os

nltk.download('punkt')

# Read the external file content
archivo_path = os.path.join(os.path.dirname(__file__), 'lab1.txt')
with open(archivo_path, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Tokenization using NLTK
palabras = nltk.word_tokenize(texto)

# Convert text to lowercase
texto = texto.lower()

# Split the text into words
palabras = texto.split()

# Print punctuation
print(string.punctuation)

# Define regex to remove punctuation
simbolos_extra = '’'
re_punc = re.compile('[%s%s]' % (re.escape(string.punctuation), re.escape(simbolos_extra)))

# Remove punctuation from each word
stripped = [re_punc.sub('', w) for w in palabras]

# Print the first 100 words
print(stripped[:100])
```

#### `lab1.4.py`

-   **Read Text File**: Reads content from `lab1.txt`.
-   **Tokenization**: Uses NLTK to tokenize the text.
-   **Convert to Lowercase**: Converts all text to lowercase.
-   **Remove Punctuation**: Removes punctuation and specific symbols from the text.
-   **Remove Stopwords**: Filters out stopwords from the text.
-   **Print Output**: Prints the first 100 words after processing.

#### Code Snippet

```python
import re
import string
import nltk
import os
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Read the external file content
archivo_path = os.path.join(os.path.dirname(__file__), 'lab1.txt')
with open(archivo_path, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Tokenization using NLTK
palabras = nltk.word_tokenize(texto)

# Split the text into words
palabras = texto.split()

print("\n///// TEXTO SIN ESPACIOS\n")
print(palabras[:100])

# Print punctuation
print("\n///// SIGNOS DE PUNTUACION\n")
print(string.punctuation)

# Define regex to remove punctuation
simbolos_extra = '’'
re_punc = re.compile('[%s%s]' % (re.escape(string.punctuation), re.escape(simbolos_extra)))

# Remove punctuation from each word
stripped = [re_punc.sub('', w) for w in palabras]

print("\n///// TEXTO SIN SIGNOS DE PUNTUACION\n")
print(stripped[:100])

# Convert each word to lowercase
for i in range(len(stripped)):
    stripped[i] = stripped[i].lower()

print("\n///// TEXTO EN MINUSCULAS\n")
print(stripped[:100])

# Get a list of stopwords in English
stopwords_english = set(stopwords.words('english'))

# Convert the set of stopwords to a list
stopwords_english_list = list(stopwords_english)

# Print the first 5 stopwords
print("\n///// PRIMERAS 5 PALABRAS VACÍAS\n")
print(stopwords_english_list[:5])

# Remove stopwords
filtered_words = [word for word in stripped if word not in stopwords_english]

# Print the first 100 words without stopwords
print("\n///// TEXTO SIN PALABRAS VACIAS\n")
print(filtered_words[:100])
```

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

-   Python 3.x
-   NLTK library

### Installation

1.  Clone the repo
    
    ```sh
    git clone https://github.com/KPlanisphere/grimm-text-processor.git
    ```
    
2.  Install the required Python packages
    
    ```sh
    pip install nltk
    ```
    

## Usage

Run each script using Python:

```sh
python lab1.1.py
python lab1.2.py
python lab1.3.py
python lab1.4.py
```

## Project Documentation

### Introduction

In this practice, Python was used to create code that, from a given text, separates the text into tokens, removes punctuation marks, converts the text to lowercase, and removes stopwords. We utilize the NLTK library and predefined code within the library that facilitates these tasks, such as `split`, `string.punctuation`, `re`, and `stopwords`.

### Objective

Learn to prepare texts for use in information retrieval processes. This involves separating the text into tokens, removing useless tokens (punctuation marks, numbers, stopwords), and converting to lowercase.

### Experimental Development

1.  **Tokenization**: Using spaces as delimiters, split the text into words and print the first 100 words.
2.  **Punctuation Removal**: Using `re` to remove punctuation marks, print the punctuation marks, and then print the first 100 words after removing punctuation.
3.  **Lowercase Conversion**: Convert the text to lowercase and print the first 100 words.
4.  **Stopwords Removal**: Import stopwords in English, print the first 5 stopwords, and then print the first 100 words after removing stopwords.

### Discussion and Results

-   Tokenization separates the text into individual words.
-   Punctuation removal cleans the text by removing punctuation marks.
-   Lowercase conversion standardizes the text.
-   Stopwords removal filters out common words that do not add much meaning.

### Conclusion

Through constant practice, we have gained a deeper understanding of handling various functions related to text processing in Python. This process has allowed us to solidify our comprehension, providing a stronger foundation for text preparation and manipulation for information retrieval using Python and the NLTK library.