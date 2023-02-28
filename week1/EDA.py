import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.rc('font', family='Malgun Gothic') # For Windows
import warnings

print(os.getcwd())
df = pd.read_csv('국민건강보험공단_건강검진정보_20211229.CSV', encoding='cp949')
