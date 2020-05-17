import ast
input_str = "{ 102:['Shiva', 24, 'Content Strategist'],104:['Udit',25,'Content Strategist'], 105:['Huzefa',32,'Project Manager' ]}"
input_dict = ast.literal_eval(input_str)
print(input_dict)
#Type you answer here
profession = input_dict['104'][2]
print(profession)
