import bokeh as bk
from bokeh.io import show
import matplotlib.pyplot as plt
import nationalaverage as avg
import pandas as pd
import os
import numpy as np

def heatmapdata():
    files = [x for x in os.listdir("../Data/DataFrames/DataFrames_Afzet_Branches") if x[-2:] == "A6"]
    heatmap = pd.DataFrame({"B1":[],"B2":[],"corr":[]})
    datums = []
    for j in range(1981,2017):
        for k in range(1,12):
            datums.append(str(j) + "MM" + "".join(str(k) if len(str(k)) == 2 else "0" + str(k)))

    for i,file1 in enumerate(files):
        path1 = os.path.join("../Data/DataFrames/DataFrames_Afzet_Branches", file1)
        df1 = pd.read_csv(path1)
        title1 = avg.titel(file1[:6])

        for file2 in files:
            path2 = os.path.join("../Data/DataFrames/DataFrames_Afzet_Branches", file2)
            df2 = pd.read_csv(path2)
            title2 = avg.titel(file2[:6])
            
            prijzen1,prijzen2 = [],[]
            for datum in datums:
                if datum in df1["Perioden"].tolist() and datum in df2["Perioden"].tolist():
                    prijs1 = df1.loc[df1["Perioden"] == datum]["ProducentenprijsindexPPI_1"].tolist()[0]
                    prijs2 = df2.loc[df2["Perioden"] == datum]["ProducentenprijsindexPPI_1"].tolist()[0]
                    if pd.notnull(prijs1) and pd.notnull(prijs2):
                        prijzen1.append(prijs1)
                        prijzen2.append(prijs2)
            
            heatmap = heatmap.append(pd.DataFrame({"B1":[title1],"B2":[title2],"corr":[int(np.correlate(prijzen1,prijzen2)[0])]}))
        print(i)
    return heatmap
if __name__ == "__main__":
    heatmapdata().to_csv("heatmap.csv")