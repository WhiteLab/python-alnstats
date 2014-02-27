from alnstats.util.plugin import dataprocessor

class FracMergeDataProcessor(dataprocessor.DataProcessor):
  '''
  Fraction of total reads merged data processor.
  '''
  name = 'FracMergeDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['fracmerge'] = 1. - (float(data['merge']) / float(data['reads']))
