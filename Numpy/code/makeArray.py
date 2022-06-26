# -*- coding: utf-8 -*-
"""
np.linspace, logspace, arange 메소드로 np.array 생성
time으로 시간을 두어 하나씩 보여준다.
@author: asna9
"""

import numpy as np
import matplotlib.pyplot as plt
import time

# np.linspace() - green 별표
a = np.linspace(0, 1, 5)
plt.plot(a, 'g*')
plt.show()

time.sleep(2)

# logspace() - 선
a = np.logspace(1, 10, num=10, base=2)
print(a)
plt.plot(a)
plt.show()

time.sleep(2)

# np.arange() - blue 별표
a = np.arange(0, 10, 2)
plt.plot(a, 'b*')
plt.show()
