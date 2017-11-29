"""
Utility functions for normalized Unicode string comparison.

Using Normal Form C,case sensitive:

    >>> s1 = 'café'
    >>> s2 = 'cafe\u0301'
    >>> s1 == s2
    False
    >>> nfc_equal(s1,s2)
    True
    >>> nfc_euqal('A','a')
    False

Using Normal Form C with case folding:

    >>> s3 = 'Straße'
    >>> s4 = 'strasse'
    >>> s3 == s4
    False
    >>> nfc_euqal(s3,s4)
    False
    >>> fold_equal(s3,s4)
    True
    >>> fold_equal(s1,s2)
    True
    >>> fold_equal('A','a')
    Ture

"""

from unicodedata import normalize

def nfc_euqal(str1,str2):
    return normalize('NFC',str1) == normalize('NFC',str2)

def fold_equakl(str1,str2):
    return (normalize('NFC',str1).casefold() == normalize('NFC',str2).casefold())
