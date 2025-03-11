from utils.functions import process
from utils.statistics import get_stat_dict
import json
from time import sleep
pict_list = ['MY FIRST SKRIPT\n\n',
              '    *********',
              '   *       **',
              '  *       * *',
              ' *********  *',
              ' *       *  *',
              ' *       *  *',
              ' *       * *',
              ' *********',
             '\n\nI LOVE PYTHON']
for i in pict_list:
     sleep(.2)
     print(i) 

with open('parallelepipeds.json', 'r') as f:
  parallelepipeds = json.load(f)

characteristics = dict()
for fig, atr_dict in parallelepipeds.items():
  a = float(atr_dict['a'])
  b = float(atr_dict['b'])
  c = float(atr_dict['c'])
  characteristics[fig] = process(a, b, c)

statistics = get_stat_dict(characteristics)

# ---Load files
with open('outputs/characteristics.json', 'w') as f:
    json.dump(characteristics, f, indent=4)


with open('outputs/statistics.json', 'w') as f:
    json.dump(statistics, f, indent=4) 

end_ = """
Created FILES:
    
    --'outputs/characteristics.json'
    -- outputs/statistics.json'

###__________END SCRIPT_________###   
"""
print(end_)
