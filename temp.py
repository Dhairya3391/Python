import matplotlib.pyplot as plt

# plt.style.use('seaborn-whitegrid')
# Set Matplotlib defaults
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)
plt.show()

# Setup feedback system
# from learntools.core import binder
# binder.bind(globals())
# from learntools.deep_learning_intro.ex1 import *