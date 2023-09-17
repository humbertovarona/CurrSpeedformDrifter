def saveCSVData(filename, DatetimeParam, LonParam, LatParam, CurrSpeedParam, CurrDirParam, CurrUParam, CurrVParam):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Date', 'Lon', 'Lat', 'Speed (m/s)', 'Dir (deg)', 'U (m/s)', 'V (m/s)'])
        for Datetime, PLons, PLats, CurrSpeed, CurrDir, CurrU, CurrV in zip(DatetimeParam, LonParam, LatParam, CurrSpeedParam, CurrDirParam, CurrUParam, CurrVParam):
            writer.writerow([Datetime, PLons, PLats, CurrSpeed, CurrDir, CurrU, CurrV])

