import pandas as pd

original = pd.read_excel('Pasta.xlsx')
clonada = original.copy()
clonada.to_excel("PlanilhaClonada.xlsx")

