
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
    
    def test_spin_words(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")
        self.assertEqual(spin_words("to"), "to")
        self.assertEqual(spin_words("CodeWars"), "sraWedoC")
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")

if __name__ == '__main__':
    unittest.main()