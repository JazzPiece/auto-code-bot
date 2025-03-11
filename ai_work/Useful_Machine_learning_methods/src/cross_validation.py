from sklearn.model_selection import cross_val_score

def cross_validate_model(model, X, y, cv):
    scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
    
    return scores