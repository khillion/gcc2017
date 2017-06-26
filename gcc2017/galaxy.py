import galaxyxml.tool as gxt
import galaxyxml.tool.parameters as gxtp
from galaxyxml.tool.import_xml import GalaxyXmlParser
from lxml import etree

def tostring(galaxyxml_object):
    return etree.tostring(galaxyxml_object.node)

def export_parameter(parameter):
    param = gxtp.DataParam(parameter.name, label=parameter.description,
                           help=parameter.help)
    return param
