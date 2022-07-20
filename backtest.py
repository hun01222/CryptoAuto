import pyupbit
import numpy as np

df=pyupbit.get_ohlcv("KRW-BTC", count=7) # OHLCV(Open, High, Low, Close, Volume: 거래량)
df['range']=(df['high']-df['low'])*0.5 # 변동폭*k값
df['target']=df['open']+df['range'].shift(1) # target: 매수가, .shift(1): range column을 한 칸 밑으로 내림

df['ror']=np.where(df['high']>df['target'], df['close']/df['target'], 1) # ror: 수익율, np.where(조건문, 참일 때 값, 거짓일 때 값)
df['hpr']=df['ror'].cumprod() # 누적수익율 계산
df['dd']=(df['hpr'].cummax()-df['hpr'])/df['hpr'].cummax()*100 # draw down 계산
print("MDD(%): ", df['dd'].max()) # max draw down
df.to_excel("dd.xlsx") # excel에 저장