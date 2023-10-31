def RemoveOutliersAndSaveCSV(input_filename, col_index, threshold=2):
    data = []
    with open(input_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data.append(header)
        for row in reader:
            data.append(row)
    column_values = [float(row[col_index]) for row in data[1:]]
    mean = statistics.mean(column_values)
    stdev = statistics.stdev(column_values)
    outlier_threshold = threshold * stdev
    cleaned_data = [data[0]]
    for row in data[1:]:
        if abs(float(row[col_index]) - mean) <= outlier_threshold:
            cleaned_data.append(row)
    if os.path.exists(input_filename):
        os.remove(input_filename)
    with open(input_filename, 'w', newline='') as output_csvfile:
        writer = csv.writer(output_csvfile)
        writer.writerows(cleaned_data)
