

import numpy as np
import pandas as pd
from sklearn.model_selection import *
import xgboost as xgb
from sklearn.metrics import mean_squared_error, explained_variance_score, roc_curve, roc_auc_score, accuracy_score, precision_score, confusion_matrix, recall_score, f1_score, auc, matthews_corrcoef
from sklearn.preprocessing import *
from sklearn.linear_model import *
from sklearn.ensemble import *
from sklearn.metrics import *
from sklearn.impute import *
from sklearn.pipeline import *
import pickle
import sys


def get_floats(source):
    for text in source.split():
        try:
            val = float(text)
            #if math.isnan(val) or math.isinf(val): continue
            yield val
        except ValueError:
            pass

clas = pickle.load(open('classifiers/classifier_red.pkl', 'rb') )

arguments = sys.argv

features = [get_floats(x) for x in arguments ]


print(clas.predict(features) )


