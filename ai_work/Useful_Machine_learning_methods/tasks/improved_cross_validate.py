from sklearn.model_selection import cross_val_score

def cross_validate_model(model, X, y, cv, scoring='accuracy'):
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    
    return scores