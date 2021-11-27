from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^KS11', '2004-01-04') #코스피 지수 데이터 다운

window = 252 #1년 개장기간 252일 어름잡아 설정
peak = kospi['Adj Close'].rolling(window, min_periods=1).max() # 종가 칼럼에서 1년 기간 단위 최고치 peak 구하기
drawdown = kospi['Adj Close']/peak - 1.0 #최고치 대비 현재KOSPI 종가가 얼마나 하락했는지 구하기
max_dd = drawdown.rolling(window, min_periods =1).min() # drawdown에서 1년 기간 단위로 최저치 max_dd를 구한다. 마이너스이기 때문에 최저치가 최대 손실 낙폭이다

plt.figure(figsize=(9, 7))
plt.subplot(211) # 2행 1열 중 1열에 그린다
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(212) # 2행 1열 중 2열에 그린다
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()
