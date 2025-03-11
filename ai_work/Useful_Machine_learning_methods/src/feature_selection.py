from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

def select_features(X, y, k_features):
    selector = SelectKBest(score_func=f_classif, k=k_features)
    X_selected = selector.fit_transform(X, y)
    
    return X_selected