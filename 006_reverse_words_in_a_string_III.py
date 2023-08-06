""" Given a string s, reverse the order of characters in each word within a sentence while still preserving
whitespace and initial word order."""

''' https://leetcode.com/problems/reverse-words-in-a-string-iii/description/ '''


def reverse_words(s):
    splited_words = s.split(' ')

    reversed_words = ""
    for index, word in enumerate(splited_words):
        if index < len(splited_words) - 1:
            reversed_words = reversed_words + ''.join(reversed(word)) + ' '
        else:
            reversed_words = reversed_words + ''.join(reversed(word))

    return reversed_words


print(reverse_words("hello world!"))
