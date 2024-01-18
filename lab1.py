import nltk
import os
nltk.download('punkt')  # Asegúrate de tener el tokenizador punkt descargado

# Lee el contenido del archivo externo
archivo_path = os.path.join(os.path.dirname(__file__), 'lab1.txt')
with open(archivo_path, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Tokenización usando NLTK
palabras = nltk.word_tokenize(texto)

palabras = texto.split()

# Imprime las primeras 100 palabras
print(palabras[:100])
