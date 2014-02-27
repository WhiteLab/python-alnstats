import parser
import settings

from alnstats.util.plugin import fileprocessor

class Casava18Processor(fileprocessor.FileProcessor):
  '''
  Casava 1.8 format file processor.
  '''
  name = 'Casava18Processor'

  def process(self,fname,**kwargs):
    '''
    Casava 1.8 format file processor.
    '''
    # Initialize data using settings defaults.
    data = dict(settings.data)

    # Parse each line as a Casava 1.8 line.
    for i,line in enumerate(parser.parse(fname)):
      # Skip the first line.
      if not i: continue

      # Pull out the length from the sequence line.
      data['len'] = len(line['seq'])

      # Break early - we only need the first sequence line.
      break

    # Return processed data.
    return data
