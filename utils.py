import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MultiLabelBinarizer

def load_banking(data_dir='datasets/', bin_label=True):
    fname = data_dir + 'bank-additional-full.csv'
    str_obj = [1,2,3,4,5,6,7,8,9,14]
    n_str = len(str_obj)
    X1 = np.genfromtxt(fname, delimiter=";", skip_header=True,
                     dtype=None, encoding=None, usecols=str_obj)
    # Map string inputs to numerical values for analysis
    # To avoid giving weights to the different label representations (obtained via
    # LabelEncoder) based on their numerical value it is sometimes good to add dummy
    # categories and have binary values such that each feature weights the same 
    if (not bin_label) :
        for i in range(n_str) :
            X1[:,i] = LabelEncoder().fit_transform(X1[:,i])
        XB = X1
    else :
        mlb = MultiLabelBinarizer()
        XB = mlb.fit_transform(X1)
#         print(mlb.classes_)

    num_obj = [0,10,11,12,13,15,16,17,18,19]
    n_num = len(num_obj)
    dtype = (float, n_num)
    X2 = np.genfromtxt(fname, delimiter=";", skip_header=True,
                     dtype=dtype, encoding=None, usecols=num_obj)


    X = np.hstack((XB,X2))

    y = np.genfromtxt(fname, delimiter=";", skip_header=True,
                     dtype=None, encoding=None, usecols=20)
    y = LabelEncoder().fit_transform(y)

    return X, y

def load_reduced_banking(data_dir='datasets/', bin_label=True, n_y_ratio = 1.):
    X, y = load_banking()
    n_y1 = 0
    for e in y:
        if e == 1 :
            n_y1 += 1
    frac_y = n_y1/len(y)
    frac_x = 1 - frac_y
    
    X_1 = []
    y_1 = []
    for i in range(len(y)):
        if y[i] == 1:
            X_1.append(X[i,])
            y_1.append(y[i])
        else :
            if (np.random.random() < frac_y*(n_y_ratio)*1.1):
                X_1.append(X[i,])
                y_1.append(y[i]) 
            
    X_keep = np.array(X_1)
    y_keep = np.array(y_1)

    return X_keep, y_keep
        
    
    

