# Código (FALLO)


def first_n_smallest(arr, n):

    lista = []
    [lista.append(num) if num in sorted(arr)[:n] and lista.count(num) < sorted(arr)[:n].count(num) else None for num in arr]

    return lista

# Testing

import unittest
class Testeo(unittest.TestCase):

    def test_first_n_smallest(self):
        self.assertEqual(first_n_smallest([1,2,3,4,5],3), [1,2,3])
        self.assertEqual(first_n_smallest([5,4,3,2,1],3), [3,2,1])
        self.assertEqual(first_n_smallest([1,2,3,1,2],3), [1,2,1])
        self.assertEqual(first_n_smallest([1,2,3,-4,0],3), [1,-4,0])
        self.assertEqual(first_n_smallest([1,2,3,4,5],0), [])
        self.assertEqual(first_n_smallest([1,2,3,4,5],5), [1,2,3,4,5])
        self.assertEqual(first_n_smallest([1,2,3,4,2],4), [1,2,3,2])
        self.assertEqual(first_n_smallest([2,1,2,3,4,2],2), [2,1])
        self.assertEqual(first_n_smallest([2,1,2,3,4,2],3), [2,1,2])
        self.assertEqual(first_n_smallest([2,1,2,3,4,2],4), [2,1,2,2])
        self.assertEqual(first_n_smallest([8, -10, 6, 5, 3, -10, 6, 9, 0, -5, 8, 7, 2, -5, 4, 5, 0, 10, 10, 0, -9, -4, 9, -6, 6, 7, -3, -1, 7, -10, 0, 7, 9, 2, 1, -4],23), [-10, 6, 5, 3, -10, 0, -5, 2, -5, 4, 5, 0, 0, -9, -4, -6, -3, -1, -10, 0, 2, 1, -4])

if __name__ == '__main__':
    unittest.main()