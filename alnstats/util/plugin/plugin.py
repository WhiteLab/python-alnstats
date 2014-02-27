class PluginMount(type):
  '''
  A simple plugin meta class.
  '''
  def __init__(cls,name,bases,attrs):
    if not hasattr(cls,'plugins'): cls.plugins = list()
    else: cls.plugins.append(cls)
