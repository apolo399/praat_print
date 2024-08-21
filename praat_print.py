import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def praat_read(file: str) -> pd.DataFrame:
    df = pd.read_csv(file, sep=' ')
    df = df.drop(df.columns[[0,1,2,4,5,7,8,9,10,11,12]], axis=1) #Drops useless columns
    # df = df.drop([0,14,15])
    return df

def praat_draw(dataframe: pd.DataFrame) -> None:

    lf_vowels = {'vowel' : ['i' , 'ɛ' , 'æ' , 'u', 'ɯ' , 'ɔ' , 'ɑ', 'y' , 'o' , 'ø' , 'e' , 'ɤ' , 'œ' , 'ʌ' , 'ɒ', 'ɶ' , 'a'],
            'F1' :     [240 , 610 , 690 , 250, 300 , 500 , 750, 235 , 360 , 370 , 390 , 460 , 585 , 600 , 700, 820 , 850],
            'F2' :     [2400, 1900, 1660, 595, 1390, 700 , 940, 2100, 640 , 1900, 2300, 1310, 1710, 1170, 760, 1530, 1610]}

    df = pd.DataFrame(lf_vowels)

    fig, ax = plt.subplots(figsize=(10,8))

    x_name = 'F2'
    y_name = 'F1'

    x = df[x_name]
    y = df[y_name]

    ax.scatter(x, y,marker="")

    xx=dataframe['F2_Hz']
    yy=dataframe['F1_Hz']

    ax.plot(xx, yy)

    for v in df.vowel.unique():
        X = df[x_name].loc[df.vowel == v]
        Y = df[y_name].loc[df.vowel == v]
        for x, y in zip(X,Y):
            ax.annotate(v,(x,y), fontsize=14)

    ax.invert_yaxis()
    ax.invert_xaxis()
    ax.set_xlabel(x_name, fontsize=16)
    ax.set_xlim((2700, 300))
    ax.set_ylabel(y_name, fontsize=16)
    ax.set_ylim((1000, 100))
    ax.yaxis.tick_right()
    ax.xaxis.tick_top()
    ax.yaxis.set_label_position("right")
    ax.xaxis.set_label_position("top")
    ax.set_title('Vowels', fontsize=18)
    ax.grid()
    #plt.savefig('my_vowel_plot.png')
    plt.xticks(np.arange(300, 2700, step=300))
    plt.show()



def main(file: str):
    df_praat = praat_read(file)
    praat_draw(df_praat)

main('puedo.txt')
    