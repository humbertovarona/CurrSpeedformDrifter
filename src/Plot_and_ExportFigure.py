def Plot_and_ExportFigure(ImgFilename, numcols=1):
    if len(ImgFilename) > 0:
        plt.savefig(ImgFilename, dpi=500)
    plt.show()
