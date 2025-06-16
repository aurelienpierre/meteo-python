# Copyright Aurélien Pierre - 2025
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
import json
import ast
from sklearn.svm import *
from sklearn.naive_bayes import *
from sklearn.neural_network import *
from sklearn.tree import *
from sklearn.linear_model import *
from sklearn.ensemble import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from joblib import load, dump
from time import time

import matplotlib.pyplot as plt

# Load the data
X = load('X.joblib')
print(X.ndim, X.shape)
y = load('y.joblib')

print(y.ndim, y.shape)

# Modèles à tester
models = [SVC(C=1., gamma="auto", kernel="poly"),
          DecisionTreeClassifier(criterion="gini", splitter="best", max_features=3),
          ExtraTreeClassifier(splitter="best", max_features=3),
          HistGradientBoostingClassifier(categorical_features=[2, 3, 4, 5], interaction_cst=[(0, 3), (1,4), (2,5)]),
          MLPClassifier(max_iter=5000, learning_rate="constant")
          ]

# Écarte aléatoirement 20 % des données pour la vérification de précision
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Affiche les stats par catégorie (confortable/inconfortable) pour chaque sous-ensemble (test/entraînement)
unique_values, counts = np.unique(y_train, return_counts=True)
print(dict(zip(unique_values, counts)))

unique_values, counts = np.unique(y_test, return_counts=True)
print(dict(zip(unique_values, counts)))

# Entraîne et benchmark chaque modèle
combinaisons = 31 * 11 * 3 * 3 * 2 * 2
for model in models:
  print("\nModel:", model.__class__.__name__)
  for num_items in [144 * 6, combinaisons, combinaisons * 2, combinaisons * 3, combinaisons * 4]:
      print(num_items, "items")

      # Entraînement
      start_time = time()
      model.fit(X_train[0:num_items], y_train[0:num_items])
      end_time = time()

      print(f"Fitting took {end_time - start_time:.5f} seconds")

      # Enregistre vers le disque pour évaluer la taille du modèle
      model_filename = f"{model.__class__.__name__}_{num_items}.joblib"
      dump(model, model_filename)

      # Test
      start_time = time()
      y_pred = model.predict(X_test)
      end_time = time()
      print(f"Prediction took {end_time - start_time:.5f} seconds")

      # Si les prédictions ne possèdent qu'une catégorie, l'entraînement a échoué
      # et on refuse complètement le résultat.
      # La catégorie "confortable" est minoritaire dans l'échantillon (environ 8 %),
      # si elle n'apparaît jamais dans les prédictions, ça n'empêchera pas la précision
      # globale de tourner autour de 91 %, mais elle est illusoire, donc on l'évacue.
      unique_values, counts = np.unique(y_pred, return_counts=True)
      if(len(unique_values) > 1):
        print(dict(zip(unique_values, counts)))
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
      else:
        print("nope")
