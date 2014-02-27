from alnstats.util.plugin import dataprocessor

class SeqOTEnrDataProcessor(dataprocessor.DataProcessor):
  '''
  Sequenced on-target enrichment data processor.
  '''
  name = 'SeqOTEnrDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['seq_ot_enr'] = float(data['aln_ot']) / float(data['len'] * data['reads'])
