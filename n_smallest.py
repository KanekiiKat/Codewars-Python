# Código

def first_n_smallest(arr, n):
    resultado = []
    copia_arr = sorted(arr)[:n]
    
    for num in arr:
        if num in copia_arr:
            resultado.append(num)
            copia_arr.remove(num)
        if len(resultado) == n:
            break
    
    return resultado

# Testing

import unittest
class Testeo(unittest.TestCase):

    def test_first_n_smallest(test):
        test.assertEqual(first_n_smallest([1,2,3,4,5],3), [1,2,3])
        test.assertEqual(first_n_smallest([5,4,3,2,1],3), [3,2,1])
        test.assertEqual(first_n_smallest([1,2,3,1,2],3), [1,2,1])
        test.assertEqual(first_n_smallest([1,2,3,-4,0],3), [1,-4,0])
        test.assertEqual(first_n_smallest([1,2,3,4,5],0), [])
        test.assertEqual(first_n_smallest([1,2,3,4,5],5), [1,2,3,4,5])
        test.assertEqual(first_n_smallest([1,2,3,4,2],4), [1,2,3,2])
        test.assertEqual(first_n_smallest([2,1,2,3,4,2],2), [2,1])
        test.assertEqual(first_n_smallest([2,1,2,3,4,2],3), [2,1,2])
        test.assertEqual(first_n_smallest([2,1,2,3,4,2],4), [2,1,2,2])


if __name__ == '__main__':
    unittest.main()