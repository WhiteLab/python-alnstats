# Data fields and initial values.
data = {
  'target' : 0, # Number of Target Base Pairs
  'aln_ot' : 0, # On-Target Aligned Base Pairs
  'cov1bp' : 0, # Target Base Pairs at >= 1 coverage
  'cov2bp' : 0, # Target Base Pairs at >= 2 coverage
  'cov8bp' : 0, # Target Base Pairs at >= 8 coverage
}

# Regex fields.
re_fields = [
  r'(?P<grp>[^\t]+)',                # Group field.
  r'(?P<cov>\d+)',                   # Coverage field.
  r'(?P<cnt>\d+)',                   # Count field.
  r'(?P<tot>\d+)',                   # Total field.
  r'(?P<pct>\d\.\d+(?:e[\+-]\d+)?)', # Percentage field.
]

# Regex field separator.
re_sep = r'\t'

# Line regex.
import re
regex = re.compile('^{regex}$'.format(regex=re_sep.join(re_fields)))

# Mappings.
mappings = {
  'grp' : str,
  'cov' : int,
  'cnt' : int,
  'tot' : int,
  'pct' : float,
}
