# Data fields and initial values.
data = {
  'reads' : 0, # Total number of reads sequenced
}

# Recognized file extensions.
import os
import re
regex = r'^.*/[^\.]*{extension}$'
extensions = [
  '.txt.gz.qs',
]
extensions = map(lambda x: re.compile(regex.format(extension=x)), extensions)
