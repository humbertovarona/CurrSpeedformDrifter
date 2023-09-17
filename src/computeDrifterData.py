def computeDrifterData(lonParam, latParam, TimedateParam):
    if len(lonParam) < 2 or len(latParam) < 2 or len(TimedateParam) < 2:
        raise ValueError("Must be provide at least two points to calculate distances and directions")
    distParamList = []
    dirParamList = []
    timeParamList = []
    for i in range(1, len(lonParam)):
        last_geopoint = (latParam[i - 1], lonParam[i - 1])
        current_geopoint = (latParam[i], lonParam[i])
        distParam = geodesic(last_geopoint, current_geopoint).meters
        distParamList.append(distParam)
        delta_lat = latParam[i] - latParam[i - 1]
        delta_lon = lonParam[i] - lonParam[i - 1]
        dirParam = (180 / math.pi) * math.atan2(delta_lon, delta_lat)
        dirParamList.append(dirParam)
        last_time = datetime.strptime(TimedateParam[i - 1], "%Y-%m-%d %H:%M:%S")
        current_time = datetime.strptime(TimedateParam[i], "%Y-%m-%d %H:%M:%S")
        timeParam = (current_time - last_time).total_seconds()
        timeParamList.append(timeParam)
    return distParamList, dirParamList, timeParamList
