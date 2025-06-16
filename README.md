Ceci est le code source utilisé pour produire mon article [Le fantasme de l'IA qui déchante](https://dev.aurelienpierre.com/posts/sciences/le-fantasme-de-lia/)


## Installation des dépendances

Un environnement d'exécution Python >= 3.11 est requis. Installez les paquets Python nécessaires :

```
pip install scikit-learn numpy matplotlip
```

## Exécution

1. Générer la base de données synthétique : exécuter `python BaseDeDonnees.py`. Les enregistrements produits sont dans le fichier `results.csv` qui sera enregistré dans le répertoire courant.
2. Préparer les données : exécuter `python PreparationDonnees.py`. Les entrées/sortie des IA sont enregistrées dans deux fichiers, `X.joblib` et `y.joblib` qui seront enregistrés dans le répertoire courant. Les IA vont donc "résoudre l'équation" `X * M = y`, avec `M` le modèle, `X` un vecteur de dimension 6, et `y` un vecteur de dimension 1.
3. Entraîner les modèles : exécuter `python Model.py`. Les performances (temps de calcul et précision) sont affichées dans la sortie standard de la console, vous pouvez les rediriger vers un fichier en exécutant `python Model.py > runtime.log`. Chaque modèle est enregistré au format `.joblib` dans le répertoire courant si vous souhaitez les tester après entraînement.
4. Afficher l'arbre de décision et le nombre de nœuds : exécuter `python Graphes.py`
