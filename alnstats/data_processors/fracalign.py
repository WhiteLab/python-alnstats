from alnstats.util.plugin import dataprocessor

class FracAlignDataProcessor(dataprocessor.DataProcessor):
  '''
  Fraction of total reads aligned data processor.
  '''
  name = 'FracAlignDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['fracalign'] = float(data['align']) / float(data['reads'])
