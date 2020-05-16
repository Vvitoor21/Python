import pandas as pd
alunos ={'Nomes':['Vitor','Caio','Eduardo','Tiago','Bruno','Fernando','Yago','Roberto'],
         'Periodo':['Noite','Manhã','Tarde','Tarde','Manhã','Manhã','Manhã','Noite'],
         'Notas':[4,9,6,5,7,2,4,10],
         'Aprovação':['não','sim','sim','não','sim','não','não','sim'],
          'Matéria':['Português','Matemática','História','Geografia','Artes','Sociologia','Artes','Matemática']
        }
df = pd.DataFrame(alunos)

print(df)
"""
      Nomes Periodo  Notas   Aprovação     Matéria
0     Vitor   Noite      4       não     Português
1      Caio   Manhã      9       sim    Matemática
2   Eduardo   Tarde      6       sim      História
3     Tiago   Tarde      5       não     Geografia
4     Bruno   Manhã      7       sim         Artes
5  Fernando   Manhã      2       não    Sociologia
6      Yago   Manhã      4       não         Artes
7   Roberto   Noite     10       sim    Matemática
"""
df.head()

df['Nomes']

df.loc[[1,2,3]]

df.loc[df['Aprovação']=='sim']
