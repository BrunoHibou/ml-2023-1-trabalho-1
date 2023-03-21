import pandas as pd 
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))



sample_customer_data = pd.read_excel("./dataset.xlsx")
sample_customer_data.info()


dropna = sample_customer_data.dropna()#retorna um Dataframe vazio aka não existem linhas com todos os dados.
dropna_columns = sample_customer_data.dropna(axis=1, how="all") #Remove as colunas que estavam vazias
dropna_005 = sample_customer_data.dropna(thresh=10) #drops all rows with less than 95% fill
duplicates = sample_customer_data.duplicated(subset=['Patient ID'])#Cria um dataframe com todas os pacientes com IDS duplicadas, nesse caso nenhum





#exibindo os valores processados
print("\n")
display(sample_customer_data.head())
print("\n")
print("info after dropping all rows with missing values")
dropna.info()
print("\n")
print("info after dropping all empty columns")
dropna_columns.info()
print("\n")
print("info after dropping all rows with less than 10 %% filled values")
dropna_005.info()
print("\n")
print("info on duplicate patients")
duplicates.info()
with pd.ExcelWriter("newdataset.xlsx") as writer:
    dropna_005.to_excel(writer)

print("plotting histogram")
#sample_customer_data.boxplot(rot=90)
aux = sample_customer_data.drop(2)
aux.boxplot(rot=90)
plt.show()
print("plotted")