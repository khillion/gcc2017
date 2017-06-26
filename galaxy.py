import galaxyxml.tool as gxt
import galaxyxml.tool.parameters as gxtp
from galaxyxml.tool.import_xml import GalaxyXmlParser

def export_parameter(parameter):
    param = gxtp.DataParam(name, label=parameter.description,
                           help=parameter.help)
    return param
