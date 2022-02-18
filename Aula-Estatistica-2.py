# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 20:32:31 2022

@author: fabio
"""
# Aula Estatística 2 UDEMY

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import t
from scipy.stats import poisson
from scipy.stats import binom
from scipy.stats import chi2_contingency
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

#%% Distribuição com t de Student
# Média de salário: R$75,00 por hora; Amostra com 9 funcionários e DP de 10
# Qual a probabilidade de selecionar um cientista de dados e o salário ser menor de R$80,00 por hora?
t.cdf(1.5, 8) #<- 8 são os graus de liberdade da amostra (9 - 1) e 1.5 é obtido através da tabela

# Qual a probabilidade de selecionar um cientista de dados e o salário ser maior de R$80,00 por hora?
t.sf(1.5, 8)

# Somatório da execução dos dois códigos
t.cdf(1.5, 8) + t.sf(1.5, 8)


#%% Distribuição de Poisson
# Média de acidentes de carro por dia: 2;
# Qual a probabilidade de ocorrerem 3 acidentes no dia?
poisson.pmf(3, 2) # Cálculo de probabilidade pontual

# Qual a probabilidade de ocorrerem 3 ou menos acidentes no dia? (<=3)
poisson.cdf(3, 2)

# Qual a probabilidade de ocorrerem mais de 3 acidentes no dia? (>3)
poisson.sf(3,2)


#%% Distribuição Binomial
# Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
# eventos, experimentos, probabilidades
binom.pmf(3, 5, 0.5)

# Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde?
# nenhuma, 1, 2, 3, ou 4 vezes seguidas?
binom.pmf(0, 4, 0.25)
binom.pmf(1, 4, 0.25)
binom.pmf(2, 4, 0.25)
binom.pmf(3, 4, 0.25)
binom.pmf(4, 4, 0.25)

# Soma das probabilidades
binom.pmf(0, 4, 0.25) + binom.pmf(1, 4, 0.25) + binom.pmf(2, 4, 0.25) + binom.pmf(3, 4, 0.25) + binom.pmf(4, 4, 0.25)

# E se forem sinais de dois tempos?
binom.pmf(0, 4, 0.5)

# Probabilidade cumulativa
binom.cdf(4, 4, 0.25)

# Concurso com 12 questões, qual a probabilidade de acertar 7 questões com 4 alternativas?
binom.pmf(7, 12, 0.25) * 100

# Probabilidade de acertar as 12 questões?
binom.pmf(12, 12, 0.25) * 100


#%% Distribuição Qui-Quadrado
# Criação da matriz com os dados e execução do teste
novela = np.array([[19, 6], [43, 32]])

# Teste de hipótese
chi2_contingency(novela)
# O segundo valor do teste representa o pvalue, quando o pvalue é maior que 0,05, não há evidência de diferença significativa
# Hipótese nula: não há diferença significativa

# Criação da matriz 2 com os dados e execução do teste
novela2 = np.array([[22, 3], [43, 32]])

# Teste de hipótese 2
chi2_contingency(novela2)
# Neste caso há uma diferença significativa (pvalue > 0,05)


#%% Teste com Anova (análise de variância entre grupos)
# Carregamento dos dados
tratamento = pd.read_csv('anova.csv', sep = ';')
tratamento.head()

# Boxplot agrupando os dados pelo remédio
tratamento.boxplot(by = 'Remedio', grid = False)

# Criação do modelo de regressão linear e execução do teste
modelo1 = ols('Horas ~ Remedio', data = tratamento).fit()
resultados1 = sm.stats.anova_lm(modelo1)
resultados1 # Coluna PR(>F) representa o valor do pvalue

# Criação do segundo modelo utilizando mais atributos e execução do teste
modelo2 = ols('Horas ~ Remedio * Sexo', data = tratamento).fit() # Para incluir outra variável, utiliza-se outro separador
resultados2 = sm.stats.anova_lm(modelo2)
resultados2

# Se houver diferença, o teste de Tukey é executado (nos casos anteriores, não há diferença)
# Execução do teste de Tukey e visualização dos gráficos com os resultados
mc = MultiComparison(tratamento['Horas'], tratamento['Remedio'])
resultado_teste = mc.tukeyhsd()
print(resultado_teste)

resultado_teste.plot_simultaneous()