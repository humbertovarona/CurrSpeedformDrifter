def addVectors(lon, lat, U, V, scale, VECcolor, VECwidth):
    plt.quiver(lon, lat, U, V, color=VECcolor, transform=ccrs.PlateCarree(), pivot='tip', angles='xy',
              scale_units='xy', scale=1.0/scale, headwidth=10, headlength=15, headaxislength=10, width=VECwidth / 1000.0)
