from C5E10 import tag
from functools import partial

print(tag)
picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='wumpus.jpeg'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)