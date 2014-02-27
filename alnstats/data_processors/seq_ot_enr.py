from alnstats.util.plugin import dataprocessor

class SeqOTEnrDataProcessor(dataprocessor.DataProcessor):
  '''
  Sequenced on-target enrichment data processor.
  '''
  name = 'SeqOTEnrDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    # Get target sizes.
    genome = 3000000000 # TODO This should be an input quantity...
    target = int(data['target'])
    # Get number of bp for each target.
    sequenced_bp = int(data['len']) * int(data['reads'])
    on_target_bp = int(data['aln_ot'])
    # Calculate fraction of each.
    frac_sizes = float(genome) / float(target)
    frac_reads = float(sequenced_bp) / float(on_target_bp)
    # Compare.
    data['seq_ot_enr'] = frac_sizes / frac_reads
