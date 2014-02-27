import settings

def parse(fname,**kwargs):
  for i,line in enumerate(open(fname)):
    # Sanity check line format.
    match = settings.regex.match(line)
    if not match: raise ValueError('line %d malformed' % i)

    # Yield the respective type-cast matched values.
    mapper = lambda p: (p[0],settings.mappings[p[0]](p[1]))
    yield dict(map(mapper,match.groupdict().items()))
