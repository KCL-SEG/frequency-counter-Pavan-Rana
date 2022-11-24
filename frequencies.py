"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    while(len(items)!=0):
        frequencies.update({items[0],items:count(items[0])})
        temp = items.count(items[0])
        tem = items[0]
        for i in range(temp):
            items.remove(tem)

    return frequencies
