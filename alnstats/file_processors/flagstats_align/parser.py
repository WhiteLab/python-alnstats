import re
import gzip
import settings

def parse(fname,**kwargs):
  '''
  Flagstats parser.
  '''
  # Data dict.
  data = dict()

  # Line regex.
  regex = r'^(?P<passed>\d+) \+ (?P<failed>\d+) (?P<tag>[^\(]*)(?: \((?P<etc>.*)\))?[^.]$'
  regex = re.compile(regex)

  # Mapping from tag to data.
  mapping = {
    'read1'                               : 'read1',
    'read2'                               : 'read2',
    'mapped'                              : 'mapped',
    'in total'                            : 'total',
    'duplicates'                          : 'dups',
    'singletons'                          : 'single',
    'properly paired'                     : 'proper',
    'paired in sequencing'                : 'paired',
    'with itself and mate mapped'         : 'mated',
    'with mate mapped to a different chr' : 'diffchr',
  } # TODO should technically handle both types of diffchr...

  for i,line in enumerate(open(fname)):
    # Sanity check line format.
    match = regex.match(line)
    if not match: raise ValueError('line %d malformed' % i)

    # Parse values.
    passed = match.group('passed')
    failed = match.group('failed')
    tag    = match.group('tag')
    etc    = match.group('etc')

    # Populate data dict based on results.
    data[mapping[tag]] = (int(passed),int(failed),str(etc))

  # Fin.
  yield data
