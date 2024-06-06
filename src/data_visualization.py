import matplotlib.pyplot as plt


def boxplot_errors(values):
    # box and whisker plot
    rmse, mae, r2 = zip(*values)
    fig=plt.figure(figsize=(10,7))
    columns = 2
    rows = 2

    # Lista de nombres de métricas
    metric_names = ["RMSE", "MAE", "R2"]

    for i, metric in enumerate([rmse, mae, r2]):
      fig.add_subplot(rows, columns, i + 1)
      plt.boxplot(metric)
      plt.title(metric_names[i])
      plt.legend(loc='best')
    plt.show()

def plot_loss(histories):
  fig=plt.figure(figsize=(10,6))
  fig.tight_layout(pad=7.0)
  fig.suptitle('Evolución del error de entrenamiento y test del modelo', fontsize=15)
  columns = 2
  rows = 1
  for i in range(len(histories)):
    history = histories[i]
    fig.add_subplot(rows, columns, i+1)
    plt.plot(history.history['loss'], label='train', marker='s', ls='--')
    plt.plot(history.history['val_loss'], label='test', marker='x', ls='--')
    plt.xlabel('# Epochs')
    plt.ylabel('Loss (MSE)')
    plt.legend(loc='best')
    plt.title('Modelo ' + str(i+1) + 'º año')
  plt.show()


def plot_metrics(histories):
  fig=plt.figure(figsize=(10,6))
  fig.tight_layout(pad=7.0)
  fig.suptitle('Evolución MSE VS MAE', fontsize=15)
  columns = 2
  rows = 1
  for i in range(len(histories)):
    history = histories[i]
    fig.add_subplot(rows, columns, i+1)
    plt.plot(history.history['val_loss'], label='val_mse', marker='s', ls='--')
    plt.plot(history.history['val_mae'], label='val_mae', marker='x', ls='--')
    plt.xlabel('# Epochs')
    plt.ylabel('Loss (MSE)')
    plt.legend(loc='best')
    plt.title('Modelo ' + str(i+1) + 'º año')
  plt.show()


def plot_pred_vs_real(real_list, preds_list):
  fig=plt.figure(figsize=(10,6))
  fig.suptitle('Comparación de valores reales y predicciones del modelo',  fontsize=15)
  fig.tight_layout(pad=7.0)
  columns = 2
  rows = 1
  for i in range(len(real_list)):
    real = real_list[i]
    preds = preds_list[i]
    fig.add_subplot(rows, columns, i+1)
    plt.plot(real[-48:], label='real', marker='s', ls='--')
    plt.plot(preds[-48:], label='preds', marker='x', ls='--')
    plt.xlabel('Time (hours)')
    plt.ylabel('Power (MW)')
    plt.legend(loc='upper left')
    plt.title('Modelo ' + str(i+1) + 'º año')
  plt.show()

def residuals_dist(residuals):
  fig=plt.figure(figsize=(7,6))
  fig.suptitle('Comparación de la distribución de los residuos del modelo',  fontsize=15)
  plt.hist(residuals)
  plt.legend(loc='best')
  plt.show()


def residuals_vs_pred(residuals, preds_list):
  fig=plt.figure(figsize=(10,6))
  fig.suptitle('Residuos vs Predicciones',  fontsize=15)
  columns = 2
  rows = 1
  for i in range(len(residuals)):
    residual = residuals[i]
    preds = preds_list[i]
    fig.add_subplot(rows, columns, i+1)
    plt.scatter(residual, preds, marker='x')
    plt.legend(loc='best')
    plt.xlabel('Valores predichos')
    plt.ylabel('Residuos')
    plt.axhline(y=0, color='r', linestyle='--')
    plt.title('Modelo ' + str(i+1) + 'º año')
  plt.show()