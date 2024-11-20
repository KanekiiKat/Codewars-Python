
# Código

def repeats(arr):

    return sum(num for num in arr if arr.count(num) == 1 )

# Testing

import unittest
class Testeo(unittest.TestCase):
    
    def test_repeats(self):
        self.assertEqual(repeats([4,5,7,5,4,8]),15)
        self.assertEqual(repeats([9, 10, 19, 13, 19, 13]),19)
        self.assertEqual(repeats([16, 0, 11, 4, 8, 16, 0, 11]),12)
        self.assertEqual(repeats([5, 17, 18, 11, 13, 18, 11, 13]),22)
        self.assertEqual(repeats([5, 10, 19, 13, 10, 13]),24)

if __name__ == '__main__':
    unittest.main()