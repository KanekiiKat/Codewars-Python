
# Código

def repeats(arr):
    conteo = {}
    for numero in arr:
        if numero in conteo:
            conteo[numero] += 1
        else:
            conteo[numero] = 1
    
    resultado = sum(num for num, count in conteo.items() if count == 1)
    return resultado

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