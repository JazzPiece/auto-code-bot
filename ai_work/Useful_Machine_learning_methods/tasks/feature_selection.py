from sklearn.feature_selection import SelectFromModel

def feature_selection(X_train, y_train, X_test, model):
    selector = SelectFromModel(model)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    
    return X_train_selected, X_test_selected