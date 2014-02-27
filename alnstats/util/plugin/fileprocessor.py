import plugin

class FileProcessor(object):
  '''
  Derived plugins should provide the following:

  name - str identifier for the plugin

  process(filename,**kwargs):
    Takes as input a filename.
    Returns a dict.
  '''
  __metaclass__ = plugin.PluginMount

  name = 'None'
