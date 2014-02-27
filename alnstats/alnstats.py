import settings
import logging

from util.plugin import fileprocessor
from util.plugin import dataprocessor

def header(**kwargs):
  return '\t'.join(settings.fields)

def alnstats(*fnames,**kwargs):
  # Set up defaults as 'N/A'
  data = dict(map(lambda x: (x,'N/A'),settings.fields))

  # Gather group data from the grouped files.
  for fname in fnames:
    logging.debug('processing file %s' % fname)

    # Run file processors over the files.
    for plugin in fileprocessor.FileProcessor.plugins:
      logging.debug('attempting processor %s' % plugin.name)
      try: data.update(plugin().process(fname,**kwargs))
      except Exception as err:
        logging.debug(err)
        continue

  # Run data processors over the data.
  for plugin in dataprocessor.DataProcessor.plugins:
    logging.debug('attempting processor %s' % plugin.name)
    try: plugin.process(data,**kwargs)
    except Exception as err:
      logging.debug(err)
      continue

  # Generate stats report line from gathered data.
  return '\t'.join(map(lambda x: '{%s}' % x, settings.fields)).format(**data)
