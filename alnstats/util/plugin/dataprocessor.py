import plugin

class DataProcessor(object):
  '''
  Derived plugins should provide the following:

  name - str identifier for the plugin

  __call__(self,data,**kwargs):
    Takes as input a dict.
    Modifies the contents of the dict.
    Returns nothing.
  '''
  __metaclass__ = plugin.PluginMount

  name = 'None'
