# Available file processors.
# Note: Import order is execution order.
from file_processors import hgacid
from file_processors import coverage
from file_processors import casava18
from file_processors import qualityscore
from file_processors import flagstats_align
from file_processors import flagstats_rmdup

# Available data processors
# Note: Import order is execution order.
from data_processors import fraccov1bp
from data_processors import fraccov2bp
from data_processors import fraccov8bp
from data_processors import avg_ot_cov
from data_processors import fracmerge
from data_processors import fracalign
from data_processors import fracrmdup
from data_processors import aln_fra_ot
from data_processors import seq_fra_ot
from data_processors import aln_ot_enr
from data_processors import seq_ot_enr

# Data fields used for stats.
fields = [
  'bid',        # Bionimbus ID
  'date',       # Run Date
  'mac',        # Run Machine
  'run',        # Run Number
  'bar',        # Barcode
  'lane',       # Lane
  'len',        # Read Length
  'reads',      # Total Reads
  'merge',      # Post-merged and Clipped Reads
  'fracmerge',  # Fraction of Total Reads Post-Merge
  'align',      # Aligned Reads
  'fracalign',  # Fraction of Total Reads Post-Align Post-Merge
  'rmdup',      # Post-Duplicate Removed Reads
  'fracrmdup',  # Fraction of Total Reads post-Rmdup Post-Align Post-Merge
  'target',     # Number of Target Base Pairs
  'aln_ot',     # On-Target Aligned Base Pairs
  'aln_fra_ot', # Fraction of Aligned Base Pairs On-Target
  'seq_fra_ot', # Fraction of Sequencing Base Pairs On-Target
  'avg_ot_cov', # Average On-Target Coverage
  'cov1bp',     # Target Base Paicov at >= 1x Cov
  'cov2bp',     # Target Base Paicov at >= 2x Cov
  'cov8bp',     # Target Base Paicov at >= 8x Cov
  'fraccov1bp', # Fraction of Target Base Paicov at >= 1x Cov
  'fraccov2bp', # Fraction of Target Base Paicov at >= 2x Cov
  'fraccov8bp', # Fraction of Target Base Paicov at >= 8x Cov
  'aln_ot_enr', # On-Target Enrichment of Aligned Base Pairs
  'seq_ot_enr', # On-Target Enrichment of Sequenced Base Pairs
]
