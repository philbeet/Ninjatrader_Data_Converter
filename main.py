import pandas as pd
import os
# Put the path to the directory where you will store your data. Don't delete the 'r' before the quotes.
path = r""
# When you run this program, it will autodetect all files with extension ".csv" and convert them.

dirlist = os.listdir(path)
for file in dirlist:
    if file.lower().endswith(".csv"):
        print(f'Converting {file}')
        print(file.lower().replace(".csv",""))
        x = pd.read_csv(fr'{path}/{file}', names=['Ticker','Date','Time','Price','Vol'])
        file = file.lower().replace(".csv", "")
        x['Date'] = '20'+ x['Date'].astype(str) + " " + x['Time'].astype(str).str.zfill(6)
        x.drop('Time',axis=1, inplace=True)
        x.to_csv(f"{path}/{file}NINJA.csv")
    else:
        pass

