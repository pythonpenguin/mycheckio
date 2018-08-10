"""
 You have a table with all available goods in the store. The data is represented as a list of dicts

Your mission here is to find the TOP most expensive goods. The amount we are looking for will be given as a first
argument and the whole data as the second one

Input: int and list of dicts. Each dicts has two keys "name" and "price"

Output: the same as the second Input argument.
"""
import collections


def bigger_price(limit, data):
    """

    :param int limit:
    :param list of dict data:
    :rtype: list
    """
    return [{"name": e[0], "price": e[1]} for e in
            collections.Counter({d["name"]: d["price"] for d in data}).most_common(limit)]
