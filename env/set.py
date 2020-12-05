import pandas as pd
import numpy as np
import schedule as s
import join

def job(xpath):
    print("Start join zoom")
    join.join_zoom(xpath)
    print("DONE")


df = pd.read_csv("../schedule_record.csv",index_col=0)
df['TIME'] = df['TIME'].astype(str).str[0:9]
df['DATE AND TIME']= df['DATE'] + ' ' + df['TIME']
df.drop(['DATE','TIME'],axis=1,inplace=True) 
df['DATE AND TIME'] = pd.to_datetime(df['DATE AND TIME'],infer_datetime_format=True)
df = df[['DATE AND TIME','VICON']]
# print(df['VICON'][1])

#time
s.every().day.at("15:29").do(job(df["VICON"][1]))
