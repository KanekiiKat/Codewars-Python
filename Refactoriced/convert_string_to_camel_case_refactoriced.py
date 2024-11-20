
# Código

def to_camel_case(text):

    return "".join(char if i == 0 else char.capitalize() for i, char in enumerate(text.replace("_", "-" ).split("-")))
 


# Testing

import unittest
class Testeo(unittest.TestCase):

    def test_to_camel_case(self):
        self.assertEqual(to_camel_case(""), "", "An empty string was provided but not returned")
        self.assertEqual(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
        self.assertEqual(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
        self.assertEqual(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")


if __name__ == '__main__':
    unittest.main()    