from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectFromModel

def improved_feature_engineering(X_train, y_train, X_test, k_features):
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', MinMaxScaler(), list(X_train.select_dtypes(include=['int', 'float']).columns))
        ])

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('selector', SelectFromModel(RandomForestClassifier())),
        ('model', RandomForestClassifier())
    ])

    pipeline.fit(X_train, y_train)
    
    X_train_selected = pipeline.named_steps['selector'].transform(X_train)
    X_test_selected = pipeline.named_steps['selector'].transform(X_test)
    
    return X_train_selected, X_test_selected