"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items)):
        if type(items[i]) is int:
            items[i] = str(items[i])

    while(len(items)!=0):
        frequencies.update({str(items[0]):items.count(items[0])})
        temp = items.count(items[0])
        tem = items[0]
        while(temp!=0):
            items.remove(tem)
            temp = temp - 1
    return frequencies
