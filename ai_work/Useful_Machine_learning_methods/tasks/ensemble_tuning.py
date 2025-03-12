from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV

def ensemble_hyperparameter_tuning(X_train, y_train, model, params, n_iter):
    if model == 'RandomForest':
        model = RandomForestClassifier()
    elif model == 'GradientBoosting':
        model = GradientBoostingClassifier()
        
    random_search = RandomizedSearchCV(model, param_distributions=params, n_iter=n_iter, cv=5, n_jobs=-1)
    random_search.fit(X_train, y_train)
    
    return random_search