def plotVectorsMap(lon, lat, U, V, min_lon, max_lon, min_lat, max_lat, scale, VECcolor, VECwidth):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([min_lon, max_lon, min_lat, max_lat], crs=ccrs.PlateCarree())
    ax.add_feature(feature.COASTLINE)
    ax.add_feature(feature.LAND, facecolor='gray', alpha=0.25)
    gl = ax.gridlines(draw_labels=True, linestyle=':', linewidth=1, alpha=0.5)
    gl.top_labels = False
    gl.right_labels = False
    gl.xlabel_style = {'size': 10, 'color': 'gray'}
    gl.ylabel_style = {'size': 10, 'color': 'gray'}
    ax.quiver(lon, lat, U, V, color=VECcolor, transform=ccrs.PlateCarree(), pivot='tip', angles='xy', scale_units='xy', scale=1.0/scale, headwidth=10, headlength=15, headaxislength=10, width=VECwidth/1000.0)

