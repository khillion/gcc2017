import cwlgen
from cwlgen.import_cwl import CWLToolParser
import ruamel

def export(cwlgen_object):
    cwl_dict = {k: v for k, v in vars(cwlgen_object).items() if v is not None and v != []}
    return (ruamel.yaml.dump(cwl_dict, Dumper=ruamel.yaml.RoundTripDumper))


def export_parameter(parameter):
    param = cwlgen.Parameter(parameter.name, label=parameter.description,
                             doc=parameter.help)
    return export(param)
