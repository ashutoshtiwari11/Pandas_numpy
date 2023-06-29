import pandas as pd
import numpy as np 
import csv

df = pd.read_csv("Pokemon.csv")
pokemon_types = df['Type 1'].unique()
df2 = pd.DataFrame(columns=['Type 1','Total','HP','Attack','Defense','Sp. Atk','Sp. Def','Speed'])
df2.set_index('Type 1', inplace=True)
s=pd.Series(['Total','HP','Attack','Defense','Sp. Atk','Sp. Def','Speed'])


for element in s:
 for t in pokemon_types:
  max_hp_pokemon= df.loc[(df['Type 1'] == t), element].idxmax()
  max_hp_pokemon_name=df.loc[max_hp_pokemon,'Name']
  df2.loc[t, element] = max_hp_pokemon_name

with open('output.csv', 'w', encoding='utf-8') as file:
  #adding plain text to csv
  writer=csv.writer(file)
  writer.writerow(["The analysed data contains the maximum valued pokemon in the respective type"])
  writer.writerow(['Total','HP','Attack','Defense','Sp. Atk','Sp. Def','Speed'])
  df2.to_csv('output.csv', index=False)

with open('output.db', 'w', encoding="utf-8") as file:
  file.write(str(df2))