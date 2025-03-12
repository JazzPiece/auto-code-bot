from sklearn.preprocessing import StandardScaler

def data_preprocessing(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    return scaled_data