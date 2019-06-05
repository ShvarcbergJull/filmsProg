import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold, cross_val_score

dirc = {}

data=pd.read_csv('movie_metadata.csv')
file = open("data.csv", "w")
datanew=data.pivot_table(columns=['movie_title','director_name','actor_1_name','actor_2_name','actor_3_name','genres','imdb_score'])
data.to_csv("dotan.dat",columns=['movie_title','director_name','actor_1_name','actor_2_name','actor_3_name','genres','imdb_score'])

