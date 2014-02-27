from alnstats.util.plugin import dataprocessor

class AvgOTCovDataProcessor(dataprocessor.DataProcessor):
  '''
  Average coverage of target data processor.
  '''
  name = 'AvgOTCovDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['avg_ot_cov'] = float(data['aln_ot']) / float(data['target'])
