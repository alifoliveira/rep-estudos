import pandas as pd

# pd.set_option('display.max_rows', 10)      # configura o limite de linhas a serem visualizadas nos dataframes
# pd.set_option('display.max_columns', 10)   # configura o limite de colunas a serem visualizadas nos dataframes


dataset = pd.read_csv('data\db.csv', sep = ';')
print(dataset[['Quilometragem', 'Valor']].describe()) # descreve colunas especificadas
print(dataset.info())                                 # exibe informações sobre os campos do dataset
