#Codewars: https://www.codewars.com/kata/525f50e3b73515a6db000b83

# Código

def create_phone_number(n):
    n = list(n)
    tnumber = ""
    tnumber.join("(" + n[0:3] + ")" + " " + n[3:6] + "-" + n[6:10])
    return tnumber


# Testing

import unittest
class Testeo(unittest.TestCase):
    def test_create_phone_number(test):
        test.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        test.assertEqual(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        test.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        test.assertEqual(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        test.assertEqual(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

if __name__ == '__main__':
    unittest.main()