import parser
import settings

from alnstats.util.plugin import fileprocessor

class HGACIDProcessor(fileprocessor.FileProcessor):
  '''
  HGAC ID processor.
  '''
  name = 'HGACIDProcessor'

  def process(self,fname,**kwargs):
    '''
    HGAC filename parser.
    '''
    # Initialize data dict using settings default.
    data = dict(settings.data)

    # Parse each line as a coverage line.
    for i,line in enumerate(parser.parse(fname)):
      bid  = line['bid']
      date = line['date']
      mac  = line['mac']
      run  = line['run']
      bar  = line['bar']
      lane = line['lane']
      pair = line['pair']

      # Update data based on parsed values.
      data['bid']  = bid
      data['date'] = date
      data['mac']  = mac
      data['run']  = run
      data['bar']  = bar
      data['lane'] = lane
      data['pair'] = pair

    # Return processed data.
    return data
