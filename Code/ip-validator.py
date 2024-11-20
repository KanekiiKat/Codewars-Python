#Codewars = https://www.codewars.com/kata/515decfd9dcfc23bb6000006

# Codigo:

def is_valid_ip(strng):
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
    
    def test_is_valid_ip(self):
        self.assertTrue(is_valid_ip('12.255.56.1'))
        self.assertFalse(is_valid_ip(''))
        self.assertFalse(is_valid_ip('abc.def.ghi.jkl'))
        self.assertFalse(is_valid_ip('123.456.789.0'))
        self.assertFalse(is_valid_ip('12.34.56'))
        self.assertFalse(is_valid_ip('12.34.56 .1'))
        self.assertFalse(is_valid_ip('12.34.56.-1'))
        self.assertFalse(is_valid_ip('123.045.067.089'))
        self.assertTrue(is_valid_ip('127.1.1.0'))
        self.assertTrue(is_valid_ip('0.0.0.0'))
        self.assertTrue(is_valid_ip('0.34.82.53'))
        self.assertFalse(is_valid_ip('192.168.1.300'))

if __name__ == '__main__':
    unittest.main()