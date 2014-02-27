# Data fields and initial values.
data = {
  'bid'  : 'N/A', # Bionimbus ID
  'date' : 'N/A', # Date of Sequencing Run
  'mac'  : 'N/A', # Machine ID
  'run'  : 'N/A', # Run Number
  'bar'  : 'N/A', # Barcode ID
  'lane' : 'N/A', # Lane Number
  'pair' : False, # Paired
}

# Regex fields.
re_fields = [
  r'(?P<bid>\d{4}-\d+)', # BID
  r'(?P<date>\d{6})',    # Date
  r'(?P<mac>[^_]+)',     # Machine
  r'(?P<run>\d{4})',     # Run
  r'(?P<bar>[^_]+)',     # Barcode
  r'(?P<lane>\d)',       # Lane
  r'?(?P<pair>\d)?',      # Pair
]

# Regex field separator.
re_sep = r'_'

# Line regex.
import re
regex = re.compile('{regex}'.format(regex=re_sep.join(re_fields)))

# Mappings.
mappings = {
  'bid'  : str,
  'date' : str,
  'mac'  : str,
  'run'  : str,
  'bar'  : str,
  'lane' : str,
  'pair' : bool,
}
