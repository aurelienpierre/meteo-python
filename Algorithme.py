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

def programme(temperature, uv, precipitations, dessous, solaire, pardessus):
    if temperature < 15 and dessous == "pull":
        pass
    elif temperature >= 15 and dessous == "T-shirt":
        pass
    else:
        return False

    if uv > 4 and solaire == "crème solaire":
        pass
    elif uv <= 4 and solaire == "rien":
        pass
    else:
        return False

    if precipitations == "sec" and pardessus == "veste":
        pass
    elif precipitations == "faibles" and pardessus == "parapluie":
        pass
    elif precipitations == "fortes" and pardessus == "imperméable":
        pass
    else:
        return False

    return True
