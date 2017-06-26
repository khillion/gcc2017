class Parameter(object):
    """
    """
    def __init__(self, name, description=None, help=None):
        self.name = name
        # Galaxy: label, CWL: doc
        self.description = description
        self.help = None
