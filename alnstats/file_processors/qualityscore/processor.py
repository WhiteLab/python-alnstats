import parser
import settings

from alnstats.util.plugin import fileprocessor

class QalityScoreProcessor(fileprocessor.FileProcessor):
  '''
  Quality score file processor.
  '''
  name = 'QualityScoreProcessor'

  def process(self,fname,**kwargs):
    '''
    Coverage file parser.
    '''
    # Initialize data dict using settings default.
    data = dict(settings.data)

    # Sanity check filename.
    for extension in settings.extensions:
      if extension.match(fname): break
    else: raise ValueError('filename does not match known extensions')

    # Parse each line as a coverage line.
    for i,line in enumerate(parser.parse(fname)):
      reads = line['reads']
      data['reads'] = reads

    # Return processed data.
    return data
