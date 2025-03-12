from sklearn.pipeline import Pipeline

def create_pipeline(model, scaler):
    pipeline = Pipeline([('scaler', scaler), ('model', model)])
    
    return pipeline