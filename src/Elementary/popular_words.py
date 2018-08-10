"""
Input: The text and the search words array.
Output: The dictionary where the search words are the keys and values are the number of times when those words are
occurring in a given text.
Precondition: The input text will consists of English letters in uppercase and lowercase and whitespaces.
"""
import collections


def popular_words(text, words):
    """

    :param str text:
    :param str words:
    :rtype: dict
    """
    cnt = collections.Counter(text.replace("\n"," ").lower().split(" "))
    return {w: cnt[w] for w in words}
