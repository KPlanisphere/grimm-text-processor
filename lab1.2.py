import re
import string
import nltk
import os

nltk.download('punkt')  # Asegúrate de tener el tokenizador punkt descargado

# Lee el contenido del archivo externo
archivo_path = os.path.join(os.path.dirname(__file__), 'prueba.txt')
with open(archivo_path, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Tokenización usando NLTK
palabras = nltk.word_tokenize(texto)

texto = texto.lower()

palabras = texto.split()

print(string.punctuation)

# Definir expresión regular para eliminar signos de puntuación
simbolos_extra =  'aeiou'
re_punc = re.compile('[%s]' % (re.escape(simbolos_extra)))

# Eliminar signos de puntuación de cada palabra
stripped = [re_punc.sub('', w) for w in palabras]

# Imprime las primeras 100 palabras
print(stripped[:100])


