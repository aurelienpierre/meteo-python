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

import random
from time import time
from Algorithme import programme
from DataTypes import *

output_file = "responses.csv"
donnees = []
inputs = []
num_elems = 1000000

# Génère toutes les combinaisons à l'avance
for _ in range(num_elems):
    triplet = [
        random.randint(0, 30),
        random.randint(0, 10),
        random.sample(Precipitations, 1)[0],
    ]
    objects = [
        random.sample(Dessous, 1)[0],
        random.sample(Solaire, 1)[0],
        random.sample(Pardessus, 1)[0],
    ]
    inputs.append([triplet, objects])

# Créée la prédiction algorithmique, séparément pour obtenir une mesure de temps d'exécution
start_time = time()
for triplet, objects in inputs:
    result = programme(
        triplet[0], triplet[1], triplet[2], objects[0], objects[1], objects[2]
    )
    donnees.append(f"{triplet} ; {objects} ; {result}")
end_time = time()

print(f"Generation took {end_time - start_time:.5f} seconds")

# Enregistre dans un fichier pour révision humaine
with open(output_file, "w") as f:
    f.write("\n".join(donnees))
