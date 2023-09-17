def selectVectors(ValueList, Step):
    Index = [i for i in range(len(ValueList)) if i % Step == 0]
    selected_values = [ValueList[i] for i in Index]
    return selected_values
