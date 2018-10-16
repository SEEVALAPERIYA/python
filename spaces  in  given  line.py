def con(s):
    it = iter(s)
    prev = next(it)
    for ele in it:
        yield prev.isspace() and not ele.isspace()
        prev = ele
    yield ele.isspace()

print(sum(con(string)))
