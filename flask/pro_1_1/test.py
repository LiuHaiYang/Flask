import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as pls
date = pd.read_csv('target_rec.csv',sep='\t', header=None, names=['Target_ID','Pin_ID','Target_IP','Target_Priority','Target_Access_DT','Target_Web_live_long','Target_Rec_DT','Target_Signal'])
