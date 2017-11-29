from C5E19 import clip_annot
from inspect import signature

sig = signature(clip_annot)
sig.return_annotation

for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':',param.name, '=', param.default)