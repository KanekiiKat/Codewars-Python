# Código

def duplicate_encode(word):
    word = word.lower()
    return "".join("(" if word.count(letra) == 1 else ")" for letra in word)

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