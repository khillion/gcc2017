class Parameter(object):
    """
    """
    def __init__(self, name, label=None, help=None):
        # Galaxy: name; CWL: id
        self.name = name
        # Galaxy and CWL have label
        self.label = label
        # Galaxy: help; CWL: doc
        self.help = help
