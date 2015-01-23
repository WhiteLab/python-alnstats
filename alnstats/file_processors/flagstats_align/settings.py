# Data fields and initial values.
data = {
  'align' : 0, # Number of reads post-align
}

# Recognized file extensions.
import os
import re
regex = r'^.*/[^\.]+{extension}$'
extensions = [
  '.srt.bam.flagstats',
]
extensions = map(lambda x: re.compile(regex.format(extension=x)), extensions)
