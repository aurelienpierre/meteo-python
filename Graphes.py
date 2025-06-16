from joblib import load
from sklearn.tree import *
import matplotlib.pyplot as plt

plt.figure()
model = load("DecisionTreeClassifier_49104.joblib")

print("nœuds:", model.get_n_leaves())
print("profondeur:", model.get_depth())

plot_tree(model)
plt.title("Arbre de décision basique")
plt.show()
