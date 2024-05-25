import pandas as pd
import numpy as np
from scipy import stats

chat_id = 818742406 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return stats.ttest_1samp(x, 500, alternative='greater').pvalue < 0.06 # Ваш ответ, True или False
