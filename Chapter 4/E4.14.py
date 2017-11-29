import unicodedata
import string

def shave_marks(txt):
    """去掉全部变音符号"""
    norm_txt = unicodedata.normalize('NFD',txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC',shaved)

def shave_marks_latin(txt):
    """把拉丁基字符中所有的变音符号删除"""
    norm_txt = unicodedata.normalize('NFC',txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
        keepers.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC',shaved)
single_map = str.maketrans(""",ƒ,†ˆ‹‘’“”•––˜›""",
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)

def dewinize(txt):
    """把Win1252符号替换成ASCII字符或序列"""
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß','ss')
    return unicodedata.normalize('NFKC',no_marks)

order = '“Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.”'
print(order)
print(shave_marks(order))
Greek = 'Zέφupoς, Zéfiro'
print(Greek)
print(shave_marks(Greek))
print(dewinize(order))
print(asciize(order))
