# Implement a method to perform basic string compression using the counts of repeated characters. (This is called run-length encoding.) For example, the string "aabcccccaaa" would become a2b1c5a3. If the “compressed” string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a–z). Specify whether your solution is case sensitive or case insensitive and what you would need to change to make it the other. Afterward, write a brief explanation walking through your code's logic in markdown.


def is_shorter(compressed_string,raw_string):
    return len(compressed_string) < len(raw_string)

def compress(str):
    case_insensitive = str.lower()






'aabbcccbbbb'
'abcdefg'
