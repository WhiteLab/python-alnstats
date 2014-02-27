from alnstats.util.plugin import dataprocessor

class PEQSDataProcessor(dataprocessor.DataProcessor):
  '''
  Paired End Quality Score data processor.
  '''
  name = 'PairedEndQualityScoreDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    if data['pair']: data['reads'] = 2*data['reads']
