# Código

def permute_a_palindrome(input):
    return sum(1 for char in set(input) if input.count(char) % 2 != 0) <= 1
        
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