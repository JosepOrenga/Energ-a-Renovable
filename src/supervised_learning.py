import numpy as np

def to_supervised(sequences, n_steps):
  # Transformamos el dataframe a array de numpy
  X, y = list(), list()
  for i in range(len(sequences)):
    # find the end of this pattern
    end_ix = i + n_steps
    # check if we are beyond the dataset
    if end_ix > len(sequences):
      break
    # gather input and output parts of the pattern
    seq_x, seq_y = sequences[i:end_ix, :-1], sequences[end_ix-1,-1]
    X.append(seq_x)
    y.append(seq_y)
  return np.array(X), np.array(y)

def prior_inverse(features, targets):
    dataset = []
    for i in range(features.shape[0]):
        last_row, target = features[i][0], targets[i]
        appended = np.append(last_row, target)
        dataset.append(appended)

    return np.array(dataset)

def invert_scale(scaler, test_x, test_y, predictions):
    # Damos el forma de los datos con los que se ha entrenado el scaler
  pred = prior_inverse(test_x, predictions)
  real = prior_inverse(test_x, test_y)

  # # Transformamos los datos a la inversa para que esten como los originales
  inv_pred = scaler.inverse_transform(pred)
  inv_real = scaler.inverse_transform(real)

  # Obtenemos solo la variable objetivo
  power_pred = inv_pred[:,-1]
  power_real = inv_real[:,-1]

  return power_pred, power_real

