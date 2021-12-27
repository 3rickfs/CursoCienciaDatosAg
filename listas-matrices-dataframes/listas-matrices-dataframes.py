# -*- coding: utf-8 -*-
"""
Listas, matrices y dataframes

Por medio de este programa se practica la creación y manipulación de listas,
matrices y dataframes

Created on Mon Dec 27 12:52:06 2021

@author: Erick Fiestas
"""

import numpy as np
import pandas as pd

print("Ejercicios de listas, matrices y dataframes")

#Listas
a = ["Hola", "mundo"]
a.append("Todo bien")
b = {"Dato1":1,"Dato2":2,"Dato3":"dato3"}
b = {"Dato1":1,"Dato2":2,"Dato3":{"Dato3.1":"dato3.1","Dato3.2":3.2}}

#Matrices
d = [[1,2,3],[4,5,6]]
c = np.array(d)
c = np.ones(3)
c = np.ones(3,np.int8)
c = [1,2,3,4]
c = [1.,2.,3.,4.]
c = np.random.rand(4,4)
c = np.random.rand(4,4)*20
c.astype('int8')
print(c)

#Dataframes
d = [[1,2,3],[4,5,6]]
d = pd.DataFrame(d)
d = pd.DataFrame(data=c)
d = pd.DataFrame(data=c,columns=['UNO','DOS','TRES'])
d = pd.DataFrame(data=c,columns=['UNO','DOS','TRES'],index=['Row1','Row2','Row3'])
d = pd.DataFrame(data=[(1,2,3)],columns=['UNO','DOS','TRES'],index=['Row1'])
d = pd.DataFrame(data=[(1,2,3),(4,5,6)],columns=['UNO','DOS','TRES'],index=['Row1','Row2'])
d.reset_index()
















