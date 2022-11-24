"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items)):
        if frequencies.keys().count(items(i))==0:
            frequencies.update({items(i):1})
        else:
            frequencies.update({items(i):frequencies.get(items(i))})
    return frequencies
