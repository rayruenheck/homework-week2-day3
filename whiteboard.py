# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence “The quick brown fox jumps over the lazy dog” is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(letters):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in letters:
            return False
    return True
print(is_pangram('the quick brown fox jumps over the lazy dog'))


# dylans way

def find_pangram(astring):
    alph_set = set(letter for letter in 'abcdefghijklmnopqrstuvwxyz')
    return len(alph_set.difference(set(astring.lower()))) < 1

        