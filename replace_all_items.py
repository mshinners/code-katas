"""Kata 7: Replace all items.

PilgrimShadow, fkb, rruellepetel

def replace_all(obj, find, replace):
  if isinstance(obj, str):
    return obj.replace(find, replace)
  elif isinstance(obj, list):
    return [x if x != find else replace for x in obj]
"""


def replace_all(obj, find, replace):
    """The function replaces a given item with its replacement."""
    if type(obj) is str:
        result = ''
        for i in obj:
            if i == find:
                result += replace
            else:
                result += i
        return result
    else:
        for i in range(len(obj)):
            if obj[i] == find:
                obj[i] = replace
        return obj
