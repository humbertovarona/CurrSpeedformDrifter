# CurrSpeedformDrifter

Computes drifter speeds

# Version

![](https://img.shields.io/badge/Version%3A-1.0-success)

# Release date

![](https://img.shields.io/badge/Release%20date-Sep%2C%2017%2C%202023-9cf)

# License

![](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

# Programming language

<img src="https://img.icons8.com/?size=512&id=13441&format=png" width="50"/>

# OS

<img src="https://img.icons8.com/?size=512&id=17842&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=122959&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=108792&format=png" width="50"/>

# Requirements

```shell
sudo apt -y install libgeos-dev
```

```shell
pip install matplotlib
pip install netCDF4
pip install cartopy
pip install geopy
pip install numpy
```

## Installation

```python
import csv
from geopy.distance import geodesic
import math
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as feature
import numpy as np
import netCDF4 as nc
from datetime import datetime
```
