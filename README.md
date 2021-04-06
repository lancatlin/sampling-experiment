# 取樣實驗

實驗不同取樣頻率對 FFT 結果之影響

## 安裝

本專案使用 Pipenv 管理依賴

```
git clone https://github.com/lancatlin/sampling-experiment.git
cd sampling-experiment
pipenv install
pipenv shell  # 進入虛擬環境
```

## 使用

看一給定取樣頻率之 FFT 結果

```
python sampling.py <取樣頻率>   # 若未提供預設為 30
```

看調整取樣頻率與 FFT 結果之動畫

```
python animation.py
```

看取樣頻率與高點位置之關係圖

```
python fft.py
```

