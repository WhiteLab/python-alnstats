from alnstats.util.plugin import dataprocessor

class SeqOTEnrDataProcessor(dataprocessor.DataProcessor):
  '''
  Sequenced on-target enrichment data processor.
  '''
  name = 'SeqOTEnrDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['seq_ot_enr'] = float(data['len'] * data['reads']) / float(data['aln_ot'])
