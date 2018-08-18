"""
 This mission is the first one of the series. Here you should find the length of the longest substring that consists
 of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb",
 "c" and "aaaa". The last substring is the longest one which makes it an answer.

Input: String.

Output: Int.

"""
import collections


def long_repeat(line):
    """

    :param str line:
    :rtype: int
    """
    max_length = 0
    for char, times in collections.Counter(line).most_common():
        if max_length > times:
            break
        while times:
            if char * times in line:
                if max_length < times:
                    max_length = times
                break
            else:
                times -= 1
    return max_length
