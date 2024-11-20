
# Código

def spin_words(sentence):

    sentence_list = sentence.split()
    return " ".join(word[::-1] if len(word) >= 5 else word for word in sentence_list)

# Testing

import unittest
class Testeo(unittest.TestCase):
    
    def test_spin_words(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")
        self.assertEqual(spin_words("to"), "to")
        self.assertEqual(spin_words("CodeWars"), "sraWedoC")
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")

if __name__ == '__main__':
    unittest.main()