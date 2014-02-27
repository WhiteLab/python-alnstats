from alnstats.util.plugin import dataprocessor

class FracCov1BPDataProcessor(dataprocessor.DataProcessor):
  '''
  Fraction of target covered at >= 1bp data processor.
  '''
  name = 'FracCov1BPDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['fraccov1bp'] = float(data['cov1bp']) / float(data['target'])
