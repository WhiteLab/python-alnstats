from alnstats.util.plugin import dataprocessor

class AlnFraOTDataProcessor(dataprocessor.DataProcessor):
  '''
  Fraction of aligned bp on-target data processor.
  '''
  name = 'AlnFraOTDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['aln_fra_ot'] = float(data['aln_ot']) / float(data['align'] * data['len'])
