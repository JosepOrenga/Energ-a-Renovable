from sklearn.preprocessing import MinMaxScaler

def train_test_split(data, n_test):
 return data[:n_test], data[n_test:]

def scale(train, test, min, max):
  # Escalamos entre 0 y 1
  SCALER = MinMaxScaler(feature_range=(0,1))

  # Entrenemos el objeto
  scaler = SCALER.fit(train)

  # Escalamos los datos
  train_scaled = scaler.transform(train)
  test_scaled = scaler.transform(test)

  return scaler, train_scaled, test_scaled