import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-STEEM", count=7)    #ohlcv(open, high, low, close, volume), 7일간
df['range'] = (df['high'] - df['low']) * 0.5    #변동폭*K = (고가-저가)*k
df['target'] = df['open'] + df['range'].shift(1)    #매수가, range zjffjqdmf gkszksTlr alxdmfh sofla(.shift(1))

#ror(수익율), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)
#누적곱 계산(cumprod) => 누적수익률
df['hpr'] = df['ror'].cumprod()

#Draw Down 계산(누적 최대값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

#MDD 계산(max dd)
print("MDD(%): ", df['dd'].max())

#엑셀로 출력
df.to_excel("dd.xlsx")