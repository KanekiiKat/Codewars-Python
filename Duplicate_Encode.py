
# Código

def duplicate_encode(word):
    word = word.lower()
    resultado = ""
    for letra in word:
        if word.count(letra) == 1:
            resultado += "("
        else:
            resultado += ")"
    
    return resultado

# Testing

import unittest
class Testeo(unittest.TestCase):
    
    def test_duplicate_encode(test):
        test.assertEqual(duplicate_encode("din"),"(((")
        test.assertEqual(duplicate_encode("recede"),"()()()")
        test.assertEqual(duplicate_encode("Success"),")())())","should ignore case")
        test.assertEqual(duplicate_encode("(( @"),"))((")

if __name__ == '__main__':
    unittest.main()