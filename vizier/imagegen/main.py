import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import numpy as np

# Set seaborn theme
sns.set_theme(style="whitegrid")
# Read dataset
df = pd.read_csv('data/alldata.csv')

def create_length_heatmap():
    global df
    ar = np.zeros((7, 24))
    for index, row in df.iterrows():
        if not type(row["time"]) is float:
            time = datetime.datetime.strptime(str(row["time"]), '%d.%m.%Y, %H.%M Uhr')
            ar[time.weekday(), time.hour] += row["length"]
    plot = sns.heatmap(ar)
    plot.figure.savefig('img/heatplot.png')
    plt.close()

def create_barplot_lengthvsrubrik():
    global df
    plot = sns.barplot(x="rubrik", y="length", data=df)
    plot.figure.savefig('img/barplot.png', dpi=1000)
    plt.close()

def create_length_heatmap_perrubrik():
    global df
    for i in df.rubrik.unique():
        ar = np.zeros((7, 24))
        for index, row in df.iterrows():
            if row["rubrik"] == i:
                if not type(row["time"]) is float:
                    time = datetime.datetime.strptime(str(row["time"]), '%d.%m.%Y, %H.%M Uhr')
                    ar[time.weekday(), time.hour] += row["length"]
        plot = sns.heatmap(ar)
        plot.figure.savefig('img/heatplot' + i + '.png')
        plt.close()

def main():
    create_barplot_lengthvsrubrik()
    create_length_heatmap()
    create_length_heatmap_perrubrik()