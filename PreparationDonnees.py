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
from joblib import dump

from DataTypes import convert_data_to_array

def try_decode(item):
    try:
        # Try to parse as a Python literal
        return ast.literal_eval(item)
    except (ValueError, SyntaxError):
        # If parsing fails, keep the original string
        return item


def load_responses():
    X = []
    y = []
    with open("responses.csv", "r") as file:
        for line in file:
            row = [x.strip() for x in line.strip().split(";")]
            parsed_row = [try_decode(item) for item in row]
            meteo, objects = convert_data_to_array(try_decode(parsed_row[0]), try_decode(parsed_row[1]))
            X.append(meteo + objects)
            y.append(parsed_row[2])
    return np.array(X, dtype=object), np.array(y, dtype=bool)


X, y = load_responses()
print(X)
print(y)

unique_values, counts = np.unique(y, return_counts=True)
print(dict(zip(unique_values, counts)))

dump(X, 'X.joblib')
dump(y, 'y.joblib')
