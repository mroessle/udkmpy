#!/usr/bin/python3

#    Data analysis tools for X-ray diffraction data obtained at
#    the KMC-3 XPP endstation of BESSY II.
#    Copyright (C) 2022 Matthias Roessle and Florin Boariu.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os, re

import xrayutilities as xu
import numpy as np
import matplotlib.pyplot as plt

import tqdm

import os
import xrayutilities as xu
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt