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

Precipitations = ["sec", "faibles", "fortes"]

def precipitations_to_int(value: str) -> int:
  for i, item in enumerate(Precipitations):
    if item == value:
      return i

  raise ValueError("Valeur inconnue")

def int_to_precipitations(index: int) -> str:
  return Precipitations[index]

Solaire = ["rien", "crème solaire"]

def solaire_to_int(value: str) -> int:
  for i, item in enumerate(Solaire):
    if item == value:
      return i

  raise ValueError("Valeur inconnue")

def int_to_solaire(index: int) -> str:
  return Solaire[index]


Pardessus = ["veste", "parapluie", "imperméable"]

def pardessus_to_int(value: str) -> int:
  for i, item in enumerate(Pardessus):
    if item == value:
      return i

  raise ValueError("Valeur inconnue")

def int_to_pardessus(index: int) -> str:
  return Pardessus[index]


Dessous = ["T-shirt", "pull"]

def dessous_to_int(value: str) -> int:
  for i, item in enumerate(Dessous):
    if item == value:
      return i

  raise ValueError("Valeur inconnue")

def int_to_dessous(index: int) -> str:
  return Dessous[index]


def convert_data_to_array(meteo: list, objects: list):
  meteo[0] = float(meteo[0])
  meteo[1] = float(meteo[1])
  meteo[2] = precipitations_to_int(meteo[2])
  objects[0] = dessous_to_int(objects[0])
  objects[1] = solaire_to_int(objects[1])
  objects[2] = pardessus_to_int(objects[2])
  return meteo, objects
