def read_NetCDF_data(NCFilename, depth_index, time_index, variablesList):
    with nc.Dataset(NCFilename, 'r') as nc_file:
        longitude = nc_file.variables[variablesList[0]][:]
        latitude = nc_file.variables[variablesList[1]][:]
        lon, lat = np.meshgrid(longitude, latitude)
        U = nc_file.variables[variablesList[2]][:]
        V = nc_file.variables[variablesList[3]][:]
        uo = U[time_index, depth_index, :, :]
        vo = V[time_index, depth_index, :, :]
    return lon, lat, uo, vo
