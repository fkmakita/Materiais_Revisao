# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:36:31 2022

@author: fabio
"""

#%% Revisão Gráficos: histograma, dispersão, boxplot, subplots

#%% Importação dos dados e pré-visualização
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snr
from mpl_toolkits.mplot3d import axes3d

base = pd.read_csv('trees.csv')
base.shape

base.head()


#%% Histograma
h = np.histogram(base.iloc[:,1], bins = 6)

# Visualização do histograma
plt.hist(base.iloc[:,1], bins = 6)
plt.title('Árvores')
plt.ylabel('Frequência')
plt.xlabel('Altura')

# Outra forma de produzir o histograma
# OBS: kde é referente a linha de densidade
snr.distplot(base.iloc[:,1], hist = True, kde = False, bins = 6, color = 'blue', hist_kws = {'edgecolor' : 'black'})

# Densidade
snr.distplot(base.iloc[:,1], hist = False, kde = True, bins = 6, color = 'blue', hist_kws = {'edgecolor' : 'black'})

# Densidade e Histograma
snr.distplot(base.iloc[:,1], hist = True, kde = True, bins = 6, color = 'blue', hist_kws = {'edgecolor' : 'black'})


#%% Gráficos de dispersão
plt.scatter(base.Girth, base.Volume, color = 'blue', facecolor = 'none', marker = '*')
plt.title('Árvores')
plt.ylabel('Volume')
plt.xlabel('Circunferência')

# Gráfico de dispersão sem markers
plt.plot(base.Girth, base.Volume)
plt.title('Árvores')
plt.ylabel('Volume')
plt.xlabel('Circunferência')

# Outra forma de produzir o gráfico de dispersão
# OBS: fit_reg é um parâmetro de linha de tendência
snr.regplot(base.Girth, base.Volume, data = base, x_jitter = 0.3, fit_reg = True)


#%% Gráfico de dispersão com legendas e cores
base = pd.read_csv('co2.csv')
base.head()

x = base.conc
y = base.uptake

unicos = list(set(base.Treatment))
unicos

for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice], label = unicos[i])
plt.legend(loc = 'lower right')


#%% Subplots
base =  pd.read_csv('trees.csv')
base.head()

# Gerando o subplot
plt.figure(1)
plt.subplot(2, 2, 1)
plt.scatter(base.Girth, base.Volume)
plt.subplot(2, 2, 2)
plt.scatter(base.Girth, base.Height)
plt.subplot(2, 2, 3)
plt.scatter(base.Height, base.Volume, marker = '*')
plt.subplot(2, 2, 4)
plt.hist(base.Volume)


#%% Boxplots
base = pd.read_csv('trees.csv')
base.head()

# Gerando o boxplot
# OBS: notch cria um destaque na mediana, showfliers exibe os outliers
plt.boxplot(base.Volume, vert = False, showfliers = True, notch = False, patch_artist = True)
plt.title('Árvores')
plt.xlabel('Volume')

# Gerando boxplot por linhas
plt.boxplot(base)
plt.title('Árvores')
plt.xlabel('Dados')

# Gerando 3 boxplots com diferentes informações
plt.boxplot(base.Volume, vert = False)
plt.boxplot(base.Girth, vert = False)
plt.boxplot(base.Height, vert = False)
plt.title('Árvores')
plt.xlabel('Dados')


#%% Gráficos de barras e de setores (pizza)
base = pd.read_csv('insect.csv')
base.shape

base.head()

# Agrupamento dos dados baseado no atributo 'spray', contando e somando os registros
agrupado = base.groupby(['spray'])['count'].sum()
agrupado

# Gráfico de barras
agrupado.plot.bar(color = 'gray')

# Definindo as cores
agrupado.plot.bar(color = ['blue', 'yellow', 'red', 'green', 'pink', 'orange'])

# Gráfico de setores
agrupado.plot.pie()

# Definindo a legenda
agrupado.plot.pie(legend = True)


#%% Boxplot através do seaborn
base = pd.read_csv('trees.csv')
base.head()

# Visualização de um boxplot
snr.boxplot(base.Volume).set_title('Árvores')

# Visualização de vários boxplots na mesma imagem
snr.boxplot(data = base)


#%% Histograma através do seaborn
base = pd.read_csv('trees.csv')
base.head()

# Histograma com 10 divisões (bins) e com gráfico de densidade
snr.distplot(base.Volume, bins = 10, axlabel = 'Volume').set_title('Árvores')

# Carregamento de outra base de dados
base2 = pd.read_csv('chicken.csv')
base2.head()

# Criação de novo dataframe agrupando o atributo 'feed
agrupado = base2.groupby(['feed'])['weight'].sum()
agrupado

# Novo dataframe somente para testar os filtros do pandas
teste = base2.loc[base2['feed'] == 'horsebean']
teste

# Histograma considerando somente o valor 'horsebean'
snr.distplot(base2.loc[base2['feed'] == 'horsebean'].weight, hist = False).set_title('horsebean')

# Histograma considerando somente o valor 'horsebean'
snr.distplot(base2.loc[base2['feed'] == 'horsebean'].weight, hist = False).set_title('horsebean')

# Histograma considerando somente o valor 'casein'
snr.distplot(base2.loc[base2['feed'] == 'casein'].weight, hist = True).set_title('casein')

# Histograma considerando somente o valor 'linseed'
snr.distplot(base2.loc[base2['feed'] == 'linseed'].weight, hist = True).set_title('linseed')

# Histograma considerando somente o valor 'meatmeal'
snr.distplot(base2.loc[base2['feed'] == 'meatmeal'].weight, hist = True).set_title('meatmeal')

# Histograma considerando somente o valor 'soybean'
snr.distplot(base2.loc[base2['feed'] == 'soybean'].weight, hist = True).set_title('soybean')

# Histograma considerando somente o valor 'sunflower'
snr.distplot(base2.loc[base2['feed'] == 'sunflower'].weight, hist = True).set_title('sunflower')

# Criação de subplot 2x3
plt.figure()
plt.subplot(3, 2, 1)
snr.distplot(base2.loc[base2['feed'] == 'horsebean'].weight, hist = True).set_title('horsebean')
plt.subplot(3, 2, 2)
snr.distplot(base2.loc[base2['feed'] == 'casein'].weight, hist = True).set_title('casein')
plt.subplot(3, 2, 3)
snr.distplot(base2.loc[base2['feed'] == 'linseed'].weight, hist = True).set_title('linseed')
plt.subplot(3, 2, 4)
snr.distplot(base2.loc[base2['feed'] == 'meatmeal'].weight, hist = True).set_title('meatmeal')
plt.subplot(3, 2, 5)
snr.distplot(base2.loc[base2['feed'] == 'soybean'].weight, hist = True).set_title('soybean')
plt.subplot(3, 2, 6)
snr.distplot(base2.loc[base2['feed'] == 'sunflower'].weight, hist = True).set_title('sunflower')
plt.tight_layout()


#%% Gráfico de dispersão com seaborn
base = pd.read_csv('co2.csv')
base.head()

# Gráfico de dispersão utilizando os atributos conc e uptake, agrupando pelo type
snr.scatterplot(base.conc, base.uptake, hue = base.Type)

# Seleção de registros específicos da base de dados
q = base.loc[base['Type'] == 'Quebec']
m = base.loc[base['Type'] == 'Mississippi']

# Subplot mostrando gráficos de cada região
plt.figure()
plt.subplot(1, 2, 1)
snr.scatterplot(q.conc, q.uptake).set_title('Quebec')
plt.subplot(1, 2, 2)
snr.scatterplot(m.conc, m.uptake).set_title('Mississippi')
plt.tight_layout()

# Refrigerado e não refrigerado
ch = base.loc[base['Treatment'] == 'chilled']
nch = base.loc[base['Treatment'] == 'nonchilled']

# Gráfico com 'chilled' e 'non chilled'
plt.figure()
plt.subplot(1, 2, 1)
snr.scatterplot(ch.conc, ch.uptake).set_title('Chilled')
plt.subplot(1, 2, 2)
snr.scatterplot(nch.conc, nch.uptake).set_title('Non Chilled')
plt.tight_layout()

# Carregamento de outro arquivo
base2 = pd.read_csv('esoph.csv')
base2

# Gráfico entre os atributos 'alcgp' e 'ncontrols' sem agrupamento
snr.catplot(x = 'alcgp', y = 'ncontrols', data = base2, jitter = False)

# Gráfico entre os atributos 'alcgp' e 'ncontrols' com agrupamento
snr.catplot(x = 'alcgp', y = 'ncontrols', data = base2, col = 'tobgp')


#%% Gráfico 3D
base = pd.read_csv('orchard.csv')
base

# Criação do gráfico 3D, indicando o atributo projection = '3d' e passando três atributos (decrease, rowpos e colpos)
figura = plt.figure()
eixo = figura.add_subplot(1, 1, 1, projection = '3d')
eixo.scatter(base.decrease, base. rowpos, base.colpos)
eixo.set_xlabel('decrease')
eixo.set_ylabel('rowpos')
eixo.set_zlabel('colpos')