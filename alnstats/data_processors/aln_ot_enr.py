from alnstats.util.plugin import dataprocessor

class AlnOTEnrDataProcessor(dataprocessor.DataProcessor):
  '''
  Aligned on-target enrichment data processor.
  '''
  name = 'AlnOTEnrDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    data['aln_ot_enr'] = float(data['len'] * data['align']) / float(data['aln_ot'])
