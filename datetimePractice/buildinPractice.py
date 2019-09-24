print(dir(), '\n\n')

print(dir(__builtins__), '\n\n')

print(__file__, '\n\n')

print(__name__, '\n\n')

print('str', dir(str(333)), '\n\n')
print('bool', dir(bool(True)), '\n\n')
print('int', dir(int(333)), '\n\n')
print('float', dir(float(333)), '\n\n')
print('list', dir(list((333,99))), '\n\n')
print('tuple', dir(tuple([333,99])), '\n\n')
print('set', dir(set([333,99])), '\n\n')
print('dict', dir(dict({'4':2})), '\n\n')
