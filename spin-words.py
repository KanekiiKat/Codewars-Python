# Codewars: https://www.codewars.com/kata/5264d2b162488dc400000001

# Código

def spin_words(sentence):
    palabras = sentence.split()
    resultado = []
    for letras in palabras:
        if len(letras) >= 5:
            resultado.append(letras[::-1])
        else:
            resultado.append(letras)
    return " ".join(resultado)

# Testing

import unittest
class Testeo(unittest.TestCase):
    
    def test_spin_words(test):
        test.assertEqual(spin_words("Welcome"), "emocleW")
        test.assertEqual(spin_words("to"), "to")
        test.assertEqual(spin_words("CodeWars"), "sraWedoC")

if __name__ == '__main__':
    unittest.main()