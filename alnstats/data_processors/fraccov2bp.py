from alnstats.util.plugin import dataprocessor

class FracCov2BPDataProcessor(dataprocessor.DataProcessor):
  '''
  Fraction of target covered at >= 2bp data processor.
  '''
  name = 'FracCov2BPDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['fraccov2bp'] = float(data['cov2bp']) / float(data['target'])
