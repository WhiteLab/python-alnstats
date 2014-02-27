from alnstats.util.plugin import dataprocessor

class FracRMDUPDataProcessor(dataprocessor.DataProcessor):
  '''
  Fraction of total reads rmdupped data processor.
  '''
  name = 'FracRMDUPDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['fracrmdup'] = 1. - (float(data['rmdup']) / float(data['align']))
