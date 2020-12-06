import pandas as pd
import numpy as np
from apscheduler.schedulers.background import BackgroundScheduler
import join
import datetime

sched = BackgroundScheduler()
sched.start()

def join(xpath):
    print("Start join zoom")
    join.join_zoom(xpath)
    print("DONE")


df = pd.read_csv("../schedule_record.csv",index_col=0)
df['TIME'] = df['TIME'].astype(str).str[0:5]
df['DATE AND TIME']= df['DATE'] + ' ' + df['TIME']
df['DATE AND TIME'] = pd.to_datetime(df['DATE AND TIME'],infer_datetime_format=True)
df = df[['DATE AND TIME','VICON']]
# print(df['DATE AND TIME'].dtypes)
# print(df['VICON'][1])


#time
sched.add_date_job(lambda:join(df['VICON'][1]),date=datetime.datetime.now())
