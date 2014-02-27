from alnstats.util.plugin import dataprocessor

class SeqFraOTDataProcessor(dataprocessor.DataProcessor):
  '''
  Fraction of sequenced bp on-target data processor.
  '''
  name = 'SeqFraOTDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['seq_fra_ot'] = float(data['aln_ot']) / float(data['reads'] * data['len'])
