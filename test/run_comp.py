import gcc2017.abstract_tool_model as abs_tm
from gcc2017.cwl import export_parameter as exp_para_cwl
from gcc2017.galaxy import export_parameter as exp_para_xml
from gcc2017.galaxy import tostring

param = abs_tm.Parameter('Nem',
                         label='Here is a label that labels',
                         help='Take this spoon to help you')

print("CWL Param VS Galaxy XML Param")
print("=" * 30)
print(exp_para_cwl(param))
print(tostring(exp_para_xml(param)).decode('utf-8'))
