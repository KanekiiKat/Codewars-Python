def is_pangram(st):
    abecdario = "abcdefghijklmnopqrstuvwxyz"
    for char in abecdario:
        if char not in st.lower():
            return False
    return True
                                
# Casos Test:

import unittest
class Testeo(unittest.TestCase):

    def test_is_pangram(self):
        self.assertEqual(is_pangram("The quick brown fox jumps over the lazy dog"), True)
        self.assertEqual(is_pangram("Cwm fjord bank glyphs vext quiz"), True)
        self.assertEqual(is_pangram("Pack my box with five dozen liquor jugs"), True)
        self.assertEqual(is_pangram("How quickly daft jumping zebras vex."), True)
        self.assertEqual(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"), True)
        self.assertEqual(is_pangram("This isn't a pangram"), False)

        

if __name__ == '__main__':
    unittest.main()