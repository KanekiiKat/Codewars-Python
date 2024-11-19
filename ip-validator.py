#Codewars = https://www.codewars.com/kata/515decfd9dcfc23bb6000006

# Codigo:

def is_valid_IP(strng):
    points = strng.split(".")
    if len(points) != 4:
        return False
    for point in points:
        if not point.isdigit():
            return False
        
        num = int(point)

        if num < 0 or num > 255:
            return False
        if point != str(num):
            return False
    return True
        
    
# Testing:

import unittest
class Testeo(unittest.TestCase):
    
    def test_is_valid_IP(test):
        test.assertEqual(is_valid_IP('12.255.56.1'),     True)
        test.assertEqual(is_valid_IP(''),                False)
        test.assertEqual(is_valid_IP('abc.def.ghi.jkl'), False)
        test.assertEqual(is_valid_IP('123.456.789.0'),   False)
        test.assertEqual(is_valid_IP('12.34.56'),        False)
        test.assertEqual(is_valid_IP('12.34.56 .1'),     False)
        test.assertEqual(is_valid_IP('12.34.56.-1'),     False)
        test.assertEqual(is_valid_IP('123.045.067.089'), False)
        test.assertEqual(is_valid_IP('127.1.1.0'),        True)
        test.assertEqual(is_valid_IP('0.0.0.0'),          True)
        test.assertEqual(is_valid_IP('0.34.82.53'),       True)
        test.assertEqual(is_valid_IP('192.168.1.300'),   False)

        
if __name__ == '__main__':
    unittest.main()