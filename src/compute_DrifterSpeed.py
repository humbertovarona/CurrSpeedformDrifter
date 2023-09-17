def compute_DrifterSpeed(distParamList, dirParamList, timeParamList):
    if len(distParamList) != len(dirParamList) or len(distParamList) != len(timeParamList):
        raise ValueError("The distance, direction and time vectors must have the same length")
    speedParamList = []
    uParamList = []
    vParamList = []
    for i in range(len(distParamList)):
        speedParam = distParamList[i] / timeParamList[i]
        speedParamList.append(speedParam)
        dir_in_radians = math.radians(90 - dirParamList[i])
        uComp = speedParam * math.cos(dir_in_radians)
        vComp = speedParam * math.sin(dir_in_radians)
        uParamList.append(uComp)
        vParamList.append(vComp)
    return speedParamList, uParamList, vParamList
