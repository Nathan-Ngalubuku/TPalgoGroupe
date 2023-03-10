#PROJET FAIT PAR LES MEMBRES DU GROUPE 17


def reverse_file(filename):
    """Overwrite given file with its contents
    line-by-line reversed"""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()
    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()