def ReadCSV(CSVFilename):
    data = []
    with open(CSVFilename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 5:
                try:
                    id = int(row[0])
                    latParam = float(row[1])
                    lonParam = float(row[2])
                    TimedateParam = row[3]
                    data.append((id, lonParam, latParam, TimedateParam))
                except ValueError:
                    pass
    return data
