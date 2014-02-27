import gzip
import settings

def parse(fname,**kwargs):
  '''
  FASTQ Casava 1.8 format file parser.

  Parameters:
    fname - FASTQ Casava 1.8 formatd file filename

  Yields:
    dict - dict of parsed line elements based on current line
  '''
  for i,line in enumerate(gzip.open(fname)):
    # Sanity check line format.
    match = settings.regexes[i%len(settings.regexes)].match(line)
    if not match: raise ValueError('line %d malformed' % i)

    # Yield the respective type-cast matched values.
    mapper = lambda p: (p[0],settings.mappings[p[0]](p[1]))
    yield dict(map(mapper,match.groupdict().items()))
