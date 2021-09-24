import pandas as pd

boletim = pd.DataFrame({'notas1': [8, 5, 9, 8, 7],
            'notas2': [8, 4, 6, 4, 5],
            'materia': ['bio', 'mat', 'por', 'qui', 'fis']
                        })

print(boletim)

boletim['media'] =  ( boletim['notas1'] + boletim['notas2'] ) // 2

print(boletim)

for index, row in boletim.iterrows():
   if row['media'] <= 6 :
       boletim.loc[index, 'situacao'] = 'REPROVADO'
   else:
       boletim.loc[index, 'situacao'] = 'APROVADO'
