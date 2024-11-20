
# Código

def to_camel_case(text):
    if not text:
        return ""
    
    nueva_cadena = ""
    convertirmayus = True

    for caracter in text:
        if convertirmayus:
            nueva_cadena += caracter.upper()
            convertirmayus = False
        elif caracter in "_-":
            convertirmayus = True
        else:
            nueva_cadena += caracter

    if text[0].islower():
        nueva_cadena = nueva_cadena[0].lower() + nueva_cadena[1:]
    
    return nueva_cadena.replace("-", "").replace("_", "")

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