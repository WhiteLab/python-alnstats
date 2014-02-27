import settings

# TODO Switch this to a TSVParser object.

def parse(fname,**kwargs):
  for i,line in enumerate(open(fname)):
    if not i: continue # Skip first line.
    line = line.strip().split('\t')
    yield {'reads':int(line[1])}
    break
