from sklearn.model_selection import GridSearchCV

def grid_search_model(model, X_train, y_train, params, cv=5, n_jobs=-1):
    grid_search = GridSearchCV(model, param_grid=params, cv=cv, n_jobs=n_jobs)
    grid_search.fit(X_train, y_train)
    
    return grid_search