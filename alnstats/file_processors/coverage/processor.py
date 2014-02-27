import parser
import settings

from alnstats.util.plugin import fileprocessor

class CoverageProcessor(fileprocessor.FileProcessor):
  '''
  Coverage histogram file processor.
  '''
  name = 'CoverageProcessor'

  def process(self,fname,**kwargs):
    '''
    Coverage file parser.
    '''
    # Initialize data dict using settings default.
    data = dict(settings.data)

    # Parse each line as a coverage line.
    for i,line in enumerate(parser.parse(fname)):
      grp = line['grp']
      cov = line['cov']
      cnt = line['cnt']
      tot = line['tot']
      pct = line['pct']

      # Update data based on parsed values.
      data['target']  = tot
      data['aln_ot'] += cov * cnt

      if cov >= 1: data['cov1bp'] += cnt
      if cov >= 2: data['cov2bp'] += cnt
      if cov >= 8: data['cov8bp'] += cnt

    # Return processed data.
    return data
