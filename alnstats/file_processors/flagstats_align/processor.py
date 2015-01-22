import parser
import settings

from alnstats.util.plugin import fileprocessor

class AlignFlagstatsProcessor(fileprocessor.FileProcessor):
  '''
  Aligned flagstat file processor.
  '''
  name = 'AlignFlagstatsProcessor'

  def process(self,fname,**kwargs):
    '''
    Alignment flagstats file processor.
    '''
    # Initialize data dict using settings default.
    data = dict(settings.data)

    # Check filename against known alignment flagstats.
    for extension in settings.extensions:
      if extension.match(fname): break
    else: raise ValueError('filename does not match known extensions')

    # Parse each line as a flagstats line.
    for i,line in enumerate(parser.parse(fname)):
      data['align'] = line['mapped'][0]

    # Return processed data.
    return data
