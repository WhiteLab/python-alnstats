import os
import settings

def parse(fname,**kwargs):
  # Sanity check the fname.
  match = settings.regex.match(os.path.basename(fname))
  if not match: raise ValueError('fname \'%s\' malformed' % fname)

  # Yield the respective type-cast matched values.
  mapper = lambda p: (p[0],settings.mappings[p[0]](p[1]))
  yield dict(map(mapper,match.groupdict().items()))
