from C5E10 import tag
import inspect
sig = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Bouledvard','src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)
print(bound_args)
for name, value in bound_args.arguments.items():
    print(name, '=', value)
del my_tag['name']
# bound_args = sig.bind(**my_tag)
