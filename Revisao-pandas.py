# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:34:18 2022

@author: fabio
"""

#%% Revisão pandas Keith Galli
import pandas as pd

#%% Carrega arquivo para dataframe Pandas
df = pd.read_csv("pokemon_data.csv")
df_xlsx = pd.read_excel("pokemon_data.xlsx")
df_txt = pd.read_csv('pokemon_data.txt', delimiter = '\t')

# Visualização dos primeiros/últimos dados
print(df.head(5))
print(df.tail(5))

#%% Leitura de dados
# Read Headers
print(df.columns)

# Read each column
print(df[['Name', 'Type 1', 'HP']])

# Read each row
print(df.iloc[0:4])

# Print do Index e coluna
for index, row in df.iterrows():
    print(index, row['Name'])

# Localizador específico por tipo
df.loc[df['Type 1'] == "Fire"]

# Reach a specific location (R, C)
print(df.iloc[2,1])

# Gera dados estatísticos (count, mean, std, min, etc)
df.describe()

# Ordena por valores e pode ser utilizada para ordenar 1 ou mais colunas
df.sort_values(['Type 1', 'HP'], ascending = [True, False])

#%% Alteração dos dados

print(df.head(5))
# Cria uma coluna nova de totais
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))

# Removendo a coluna de totais
df = df.drop(columns = ['Total'])
print(df.head(5))

# Outra forma de criar a coluna de totais
df['Total'] = df.iloc[:, 4:10].sum(axis = 1) # axis = 1 soma na horizontal, 0 na vertical
print(df.head(5))

# Rearranjar a posição das colunas
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5))

# Salva o DataFrame para um .csv
df.to_csv('modified.csv', index = False)

# Salva o DataFrame para um .xlsx
df.to_excel('modified.xlsx', index = False)

# Salva o DataFrame para um .txt
df.to_csv('modified.txt', index = False, sep = '\t')

#%% Filtragem dos dados
# Localizador específico
new_df = df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == "Poison") & (df['HP'] > 70)]
print(new_df)

# Reseta a numeração do index
new_df.reset_index(drop = True, inplace = True)
print(new_df)

# Localizador de parte textual
df.loc[df['Name'].str.contains('Mega')] # Localiza Mega
df.loc[~df['Name'].str.contains('Mega')] # Localiza tudo exceto Mega

import re
df.loc[df['Type 1'].str.contains('Fire|Grass', regex = True)] # Localiza Fire ou Grass
df.loc[df['Type 1'].str.contains('fiRE|gRaSS', flags = re.I, regex = True)] # Localiza Sem Case Sensitive

# Localiza nomes que comecem com pi
df.loc[df['Name'].str.contains('^pi[a-z]*', flags = re.I, regex = True)]

#%% Alterações condicionais
# Altera o tipo de Fire para Flamer
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(df.head(10))

df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'
print(df.head(10))

# Alteração com condição
df['Total'] = df.iloc[:, 4:10].sum(axis = 1) # axis = 1 soma na horizontal, 0 na vertical
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']
print(df.head(10))

#%% Groupby - Estatísticas de grupo
df = pd.read_csv("pokemon_data.csv")

# Calcula média de grupos e ordena de forma decrescente
df.groupby(['Type 1']).mean().sort_values('HP', ascending = False)

# Conta por tipo
df['count'] = 1
df.groupby(['Type 1', 'Type 2']).count()['count']

#%% Working with large amounts of data
# Carrega o DataFrame em chunks
for df in pd.read_csv('pokemon_data.csv', chunksize = 10):
    print('chunk df')
    print(df)

new_df = pd.DataFrame(columns = df.columns)

# Criação de um novo DataFrame mais enxuto
for df in pd.read_csv('pokemon_data.csv', chunksize = 5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df, results])