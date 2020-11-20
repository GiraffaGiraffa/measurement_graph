# MEASUREMENT_GRAPH

## Install requirements
```
numpy
matplotlib
pandas
```

## 함수 설명
### csv_data
WaveForms를 사용할때만 사용 가능.

csv file의 경로를 인자로 넣어주면 V1, V2, Time을 key로 가지는 python dictionary를 return한다.

각각 V1, V2, Time의 numpy array를 가지고 있다.

### Plot
인자는 다음과 같다.
X, Y, X_unit, Y_unit, X_name, Y_name, graph_name, save_path, linear_fit = False, File_format = 'pdf'

X : X data(array)

Y : Y data(array)

X_unit : X의 단위

Y_unit : Y의 단위

graph_name : 저장되는 그래프의 이름

save_path : 저장되는 그래프의 경로

linear_fit : 선형회귀 그래프를 사용할 것이면 True. default는 False이다.

File_format : jpg, png, pdf등이 가능. default는 'pdf'이다.

단위를 스케일링해서 플롯해준다. latex 형태의 input은 $(수식)$으로 사용 가능하다.

## run tutorial

1. Do example.py

![Alt text](/paper/figure/example.jpg)