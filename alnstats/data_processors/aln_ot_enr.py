from alnstats.util.plugin import dataprocessor

class AlnOTEnrDataProcessor(dataprocessor.DataProcessor):
  '''
  Aligned on-target enrichment data processor.
  '''
  name = 'AlnOTEnrDataProcessor'

  @classmethod
  def process(cls,data,**kwargs):
    # Get target sizes.
    genome = 3000000000 # TODO This should be an input quantity...
    target = int(data['target'])
    # Get number of bp mapped to each target.
    rm_mapped_bp = int(data['len']) * int(data['rmdup'])
    on_target_bp = int(data['aln_ot'])
    # Calculate fraction of each.
    frac_sizes = float(genome) / float(target)
    frac_reads = float(rm_mapped_bp) / float(on_target_bp)
    # Compare.
    data['aln_ot_enr'] = frac_sizes / frac_reads
