# Código

def permute_a_palindrome(input):
    conteo = {}
    if input == input[::-1]:
        return True
    else:    
        for letra in input:
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1
        impares = 0
        for cuenta_impares in conteo.values():
            if cuenta_impares % 2 != 0:
                impares += 1
        if impares > 1:
            return False

    return True
        
# Testing

import unittest
class Testeo(unittest.TestCase):
    
    def test_permute_a_palindrome(self):
        self.assertTrue(permute_a_palindrome("a"))
        self.assertTrue(permute_a_palindrome("aa"))
        self.assertTrue(permute_a_palindrome("aaa"))
        self.assertTrue(permute_a_palindrome("baa"))
        self.assertTrue(permute_a_palindrome("aab"))
        self.assertFalse(permute_a_palindrome("baabcd"))
        self.assertFalse(permute_a_palindrome("racecars"))
        self.assertFalse(permute_a_palindrome("abcdefghba"))
        self.assertTrue(permute_a_palindrome(""))

if __name__ == '__main__':
    unittest.main()