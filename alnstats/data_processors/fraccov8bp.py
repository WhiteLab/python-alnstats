from alnstats.util.plugin import dataprocessor

class FracCov8BPDataProcessor(dataprocessor.DataProcessor):
  '''
  Fraction of target covered at >= 8bp data processor.
  '''
  name = 'FracCov1BPDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['fraccov8bp'] = float(data['cov8bp']) / float(data['target'])
