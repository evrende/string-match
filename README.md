# string-match

**string\_match.py** is a text-based toy program written in Python (version 3.12) for generating long (100,000+ character) strings and testing them for the presence of substrings chosen and typed in by the user. A given substring will be found zero or more times in the long string, and the user will be able to see exactly how many times each chosen substring occurs. Each long string is randomly generated. Further details are provided in the source code of **string\_match.py** and its helper file **string\_match\_aux.py**. Be sure to download this second file and save it in the same folder as **string\_match.py**, as it will likely be needed!

To run and use the function in **string\_match.py**, open a terminal emulator on your device and invoke your version of Python (3):

**$ python3**

(or just **python**, depending on your system)

At the **>>>** prompt, enter

**from string\_match import main**

You can call this **main** function as many times as desired. A default value of 1,000,000 (without the commas) is provided as **main**'s single parameter, but you may provide any other integer value in calling it. Thus,

**\>>> main()**

will generate a long string of one million randomly generated letters, while

**\>>> main(200000)**

will generate one with 200,000.

It is hoped that users will derive some amusement from this small program. I personally am impressed at the speed with which the responses to queries about short submitted strings are provided. Students of probability can test or confirm their intuitions about the likelihood of given strings being present in the long one. A possible game could involve trying to find the longest meaningful substring occurring in whichever long string was generated. Have fun!

evrende
