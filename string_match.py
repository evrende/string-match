
"""
string_match.py

This module holds one function ('main')
that generates long random strings that users
can check for the presence of chosen substrings.

A helper file is also referred to (string_match_aux.py) and may be needed.
It should thus be kept in the same directory as this file.
"""

def main(n: int = 1000000): # (default value: 1 million)
    """
    Each time this function is called, a string of length n will be generated
    automatically. A minimum length of 100,000 is enforced to make using the
    function more interesting. This 'long string' is composed of all 26 letters 
    from the English alphabet, all in lowercase, and in randomized order.

    The purpose of the function is to allow users to enter various short strings
    and check the long string to see how many times a given shorter one occurs.

    By default, the long string will be generated based on actual usage frequencies
    of the 26 letters of the alphabet. Users may also request a version of the long
    string in which each letter is as likely to be present as any other.

    Only lowercase letters from the English alphabet will occur in the long string;
    spaces will not occur.
    """
    from random import choice, random
    from time import sleep
    from os import system

    # ensure proper type for calling argument:
    if (type(n) != int):
        n = 1000000

    print("The long string will reflect actual English letter frequency,")
    uniform = input("unless you Enter s here: ")

    if (uniform == "s"):
        # let source be all letters of alphabet:
        fund = [chr(x) for x in range(97, 97 + 26)]
        print("All letters in the long string will occur with equal probability.")

    else:
        from string_match_aux import f_list
        # let source reflect actual frequencies:
        fund = f_list

    min_size = 100000
    long_string, helper = "", ""

    if (n < min_size):
        n = min_size

    # fill long_string:
    while (len(long_string) < n):
        for i in range(min_size):
            helper += choice(fund)
        long_string += helper
        helper = ""

    # trim it if warranted:
    if (len(long_string) > n):
        long_string = long_string[:n]

    print("String generated! Enter test strings to check for their presence.")
    print("To exit, enter DONE or QUIT as your test string.")

    while "playing":
        # let user check for different strings:
        test = input("try this: ")
        if (test in ("DONE", "QUIT")):
            break
        this_many = long_string.count(test)
        s = "s" if (this_many != 1) else ""
        print(f"'{test}' occurs {this_many} time{s}")
        if (random() < 0.04):
            from string_match_aux import add_commas
            print(f"(list length: {add_commas(n)})")

    print("Thanks for playing!")
    sleep(1.5)
    system("clear")

