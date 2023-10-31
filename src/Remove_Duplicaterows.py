def Remove_Duplicaterows(data):
    filtered_data = [data[0]]
    for i in range(1, len(data)):
        current_row = data[i]
        prev_row = data[i - 1]
        current = str(current_row).split(',')
        prev = str(prev_row).split(',')
        if current[3] != prev[3]:
            filtered_data.append(current_row)
    return filtered_data
