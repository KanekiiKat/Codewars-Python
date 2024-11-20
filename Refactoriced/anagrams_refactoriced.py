
# Código

def anagrams(word, words):
    return [p for p in words if sorted(p) == sorted(word)]

