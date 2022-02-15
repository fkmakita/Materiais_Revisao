# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:36:19 2022

@author: fabio
"""

# Revisão de estatísticas UDEMY

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from scipy import stats
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt

base = pd.read_csv('iris.csv')
base.head()

base.shape

#%% Amostragem Simples
# Mudança da semente aleatória randômica para manter os resultados em várias execuções
np.random.seed(2345)

# Geração de um vetor aleatório de 0s e 1s com probabilidades distintas
amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p = [0.7, 0.3])

len(amostra)
len(amostra[amostra == 1])
len(amostra[amostra == 0])

# Seleção da amostra seguindo o vetor de seleção
base_final = base.loc[amostra == 0]
base_final.shape


#%% Amostragem Sistemática
# Criação das variáveis para representar a população, a amostra e o valor k
populacao = 150
amostra = 15
k = int(np.ceil(populacao/amostra))
print(k)

# Definição do valor randômico para inicializar a amostra, iniciando em 1 até k + 1
r = np.random.randint(low = 1, high = k + 1, size = 1)
print(r)

# Criação de laço para somar os próximos valores, baseado no primeiro valor r que foi definido acima
acumulador = r[0]
sorteados = []
for i in range(amostra):
    print(sorteados)
    sorteados.append(acumulador)
    acumulador += k
print(sorteados)

len(sorteados)

# Seleção da amostra seguindo o vetor de seleção
base_final = base.loc[sorteados]
base_final


#%% Amostragem Estratificada
iris = pd.read_csv('iris.csv')
iris.head()

# Contagem dos tipos de classe
iris['class'].value_counts()

# iris.iloc[:, 0:4] <- busca apenas os atributos previsores, ou seja, dados sobre pétala e sépala da planta
# iris.iloc[:, 4]   <- busca apenas a classe, ou seja, a espécie da planta
# test_size = 0.5   <- seleção de 50% da base de dados que serão copiados para x e y
# A função retorna 4 valores, entretanto serão utilizados apenas 50% da base de dados, preenchendo os outros valores com "_"
# stratify          <- retorna a amostra baseada na classe

x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], test_size = 0.5, stratify = iris.iloc[:, 4])

infert = pd.read_csv('infert.csv')
infert.head()

infert['education'].value_counts()

# Geração de uma amostra com apenas 40% dos registros
x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size = 0.6, stratify = infert.iloc[:, 1])

y1.value_counts()


#%% Medidas de centralidade e variabilidade
jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
np.mean(jogadores)

np.median(jogadores)

# Geração dos quartis
quartis = np.quantile(jogadores, [0, 0.25, 0.50, 0.75, 1])
quartis

# Desvio padrão e visualização de estatísticas
np.std(jogadores, ddof = 1)
stats.describe(jogadores)


#%% Distribuição Normal
# Conjunto de objetos em uma cesta, a média é 8, o DP é 2
# Qual a probabilidade de tirar um objeto que o peso seja menor que 6?
norm.cdf(6, 8, 2)

# Qual a probabilidade de tirar um objeto que o peso é maior que 6?
norm.sf(6, 8, 2)
1 - norm.cdf(6, 8, 2) # Outra forma de calcular

# Qual a probabilidade de tirar um objeto que o peso é menor que 6 ou maior que 10?
norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

# Qual a probabilidade de tirar um objeto que o peso é menor que 10 ou maior que 8?
norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)


#%% Teste de distribuição normal
# Criação de uma variável com dados em uma distribuição normal
dados = norm.rvs(size = 1000)
dados

# Histograma
plt.hist(dados, bins = 20)
plt.title('Dados')

# Geração de gráfico para verificar se a distribuição é normal <- Verificação visual
fig, ax = plt.subplots()
stats.probplot(dados, fit = True, plot = ax)
plt.show()

# Execução do teste de Shapiro-Wilk
# Caso o valor de p seja superior a 0.05, não podemos rejeitar a hipótese nula (dados normalmente distribuidos)
stats.shapiro(dados)

# Dados não normais
dados2 = skewnorm.rvs(4, size = 1000)

# Histograma
plt.hist(dados2, bins = 20)
plt.title('Dados')

# Geração de gráfico para verificar se a distribuição é normal <- Verificação visual
fig, ax = plt.subplots()
stats.probplot(dados2, fit = True, plot = ax)
plt.show()

# Execução do teste de Shapiro-Wilk
# Caso o valor de p seja inferior a 0.05, podemos rejeitar a hipótese nula (dados normalmente distribuidos)
stats.shapiro(dados2)