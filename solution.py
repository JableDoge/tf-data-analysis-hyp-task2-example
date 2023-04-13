import pandas as pd
import numpy as np


chat_id = 707776914 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    xm=x.mean()
    ym=y.mean()
    xd=x.var()
    yd=y.var()

    ans=abs((xm-ym)/(np.sqrt(xd+yd)))
    result = True
    if ans < alpha:
      result = False
    
    return result # Ваш ответ, True или False
