import csv
from IPython.display import display
import pandas as pd


domain_price = {}
domain_authority ={}
with open("domain_price.csv" , mode='r') as inp:
    reader=csv.reader(inp)
    domain_price_dict = {rows[0]:rows[1] for rows in reader}

with open("domain_authority.csv",mode='r') as inp:
    reader=csv.reader(inp)
    domain_authority_dict = {rows[0]:rows[1] for rows in reader}
# Merge dictionaries and keep values of common keys in list'''


    merged = {**domain_price_dict, **domain_authority_dict}
    for key, value in merged.items():
        if key in domain_price_dict and key in domain_authority_dict:
            merged[key] = [value , domain_price_dict[key]]
print(merged)

#df = pd.DataFrame(merged, columns = ['Domain','Domain Authority', 'Price'])
#df.to_csv()
#in this moment of time programmer though "wait it's easier to do it in exel".