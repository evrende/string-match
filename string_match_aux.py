"""
string_match_aux.py

for use with string_match.py

provided here:
 a list (f_list) containing letters in accordance with their frequency of use in English
 a function (add_commas) for inserting commas into integers of sufficient size
"""
freqs = {
  'e': 1202,'t': 910, 'a': 812,
  'o': 768, 'i': 731, 'n': 695,
  's': 628, 'r': 602, 'h': 592,
  'd': 432, 'l': 398, 'u': 288,
  'c': 271, 'm': 261, 'f': 230,
  'y': 211, 'w': 209, 'g': 203,
  'p': 182, 'b': 149, 'v': 111,
  'k': 69,  'x': 17,  'q': 11,
  'j': 10,  'z': 7
} # source: https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html

f_list = []

for letter in freqs:
    f_list += freqs[letter] * [letter]
# thus ready to go


def add_commas(n: int):
    """
    given integer n,
    return a string version of same,
    but with commas set to mark off thousands
    (as needed)
    """
    # handle special case:
    if (n < 1000):
        return str(n)

    # recast n:
    as_string = str(n)

    # initialize variables:
    with_commas, counter = "", 0

    while (as_string):
        # break last from as_string
        digit = as_string[-1] # save as digit
        as_string = as_string[:-1]
        # add digit to new string:
        with_commas = digit + with_commas
        counter += 1
        # set comma & reset counter as needed:
        if (counter == 3 and len(as_string) > 0):
            with_commas = "," + with_commas
            counter = 0
    return with_commas

