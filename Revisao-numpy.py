# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:12:35 2022

@author: fabio
"""

#%% Revisão numpy UDEMY
import numpy as np

#%% Criação de matriz unidimensional (1D)
mt = np.array([12,23,34,45])
print(mt)
print(type(mt))

#%% Criação de array especifico (ex: float de 64 bits)
mtfloat = np.array([1, 2, 3, 4], dtype = np.float64)
print(mtfloat)
print(type(mtfloat))

mtint = np.array([1, 2, 3, 4], dtype = np.int32)
print(mtint)
print(type(mtint))

#%% Alterar o tipo de array
mtnew = np.array([1.4, 2.1111, 3.222222, 3.99999])
print(mtnew)
mtnewint = mtnew.astype(np.int32)
print(mtnewint)

mt5 = np.array([1, 2, 3, 4])
print(mt5)
mt6 = mt5.astype(np.float64)
print(mt6)

#%% Criação de matriz bidimensional
mt7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mt7)

#%% Criação de arrays vazios tipificados
# OBS: empty significa que não são inicializados, não que são vazios
vazio = np.empty([3, 2], dtype = int)
print(vazio)

# Criação de array de zeros
zeros = np.zeros([4, 3])
print(zeros)

# Criação de array de uns
um = np.ones([5, 7])
print(um)

# Criação de matriz identidade
diagonal = np.eye(5)
print(diagonal)

#%% Criação de valores aleatórios
# Valores aleatórios entre 0 e 1
ale = np.random.random((5))
print(ale)

# Valores aleatórios contendo negativos
ale2 = np.random.randn((5))
print(ale2)

# Valores aleatórios 3 x 4
ale3 = 10*np.random.random((3,4))
print(ale3)

#%% Outros métodos para criação de números aleatórios
# Uso de seed <- vincula os números aleatórios criados com o parâmetro dentro do default_rng()
gnr = np.random.default_rng(1)
ale4 = gnr.random(3)
print(ale4)

# Uso de seed para inteiros
ale5 = gnr.integers(10, size = (3,4))
print(ale5)

#%% Método unique <- remove repetições
j = np.array([22, 23, 11, 12, 13, 13, 11, 14, 14, 15, 14, 15, 16, 17, 17, 23])
j = np.unique(j)
print(j)

#%% Funções específicas
k = np.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(k)
print(k[1, 1])
print(k.shape)
print(k[1, 1].dtype)

#%% Funções matemáticas
print(k.max())
print(k.min())
print(k.mean())
print(k.std())

#%% Funções universais
k1 = np.array([0, 1, 2, 4, 9, 36, 25])
print(np.sqrt(k1))
print(np.exp(k1))

#%% Extração de elementos
m = np.array([1, 2, 3, 4, 5, 6])
print(m[1])
print(m[0:2])
print(m[1:])
print(m[-3:])

#%% Extração de linhas e colunas
mt8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mt8)

# Primeira linha, todas colunas
mt_linha1 = mt8[0, :]
print(mt_linha1)

# Segunda linha, todas colunas
mt_linha2 = mt8[1, :]
print(mt_linha2)

# Primeira coluna, todas linhas
mt_col1 = mt8[:, 0]
print(mt_col1)

# Segunda coluna, todas linhas
mt_col2 = mt8[:, 1]
print(mt_col2)

#%% Adição e multiplicação de matrizes
ab = np.array([[1, 2], [3, 4]])
cd = np.array([[5, 6], [7, 8]])
ef = np.array([10, 20])

# Adições
print(ab + cd)
# OBS: É possível somar matriz 1D com nD
print(ab + ef)

# Multiplicação de elemento por elemento
print(ab * cd)

#%% Transposição e rearranjo de conjunto de elementos
mt9 = np.arange(15).reshape((3,5))
print(mt9)
mt9_T = mt9.T
print(mt9_T)

# Outra forma de realizar a transposição
mt9_T2 = mt9.transpose((1, 0))
print(mt9_T2)

#%% Expressões lógicas
# Usando where
v = np.random.randn(4, 4)
print(v)

x = (v > 0)
print(x)

z = np.where(x > 0, 1, -1)
print(z)