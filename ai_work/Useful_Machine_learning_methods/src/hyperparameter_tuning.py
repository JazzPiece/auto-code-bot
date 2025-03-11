from sklearn.model_selection import RandomizedSearchCV

def hyperparameter_tuning(model, X_train, y_train, params, n_iter):
    random_search = RandomizedSearchCV(model, param_distributions=params, n_iter=n_iter, cv=5, n_jobs=-1)
    random_search.fit(X_train, y_train)
    
    return random_search