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

## Usage example

```python
csvData = "/Users/varona/Laboro/pythonProject/CurrSpeedformDrifter/track1.csv"
    drifterData = ReadCSV(csvData)
    lonsData = [row[1] for row in drifterData]
    lonList = lonsData[1:]
    latsData = [row[2] for row in drifterData]
    latList = latsData[1:]
    timedateData = [row[3] for row in drifterData]
    timesList = timedateData[1:]

    DistList, DirList, TimeList = computeDrifterData(lonsData, latsData, timedateData)
    speedList, uList, vList = compute_DrifterSpeed(DistList, DirList, TimeList)

    saveCSVData("/Users/varona/Laboro/pythonProject/CurrSpeedformDrifter/track1_output.csv", timesList, lonsData, latsData, speedList, DirList, uList, vList)

    NCFilename = "/Users/varona/Laboro/pythonProject/CurrSpeedformDrifter/cmems.nc"
    variablesList = ['longitude', 'latitude', 'uo', 'vo']
    NCLon, NCLat, NCu, NCv = read_NetCDF_data(NCFilename, 0, 7, variablesList)
    plotVectorsMap(NCLon, NCLat, NCu, NCv, -62, -52, -65, -59, 0.5, 'blue', 0.25)

    indexes = get_DayIndexes(timedateData, "2022-02-21")
    dlonList = get_values_from_indices(lonList, indexes)
    dlatList = get_values_from_indices(latList, indexes)
    duList = get_values_from_indices(uList, indexes)
    dvList = get_values_from_indices(vList, indexes)
    addVectors(selectVectors(dlonList, 5), selectVectors(dlatList, 5), selectVectors(duList, 5), selectVectors(dvList, 5), 0.5, 'green', 0.25)

    Plot_and_ExportFigure('/Users/varona/Laboro/pythonProject/CurrSpeedformDrifter/compH.jpeg')
```
