from math import sqrt
from sklearn.metrics import mean_squared_error
from data_visualization import boxplot_errors, plot_loss, plot_metrics, plot_pred_vs_real, residuals_dist, residuals_vs_pred
import pandas as pd
from numpy import mean
from numpy import std


# root mean squared error or rmse
def measure_rmse(actual, predicted):
  return sqrt(mean_squared_error(actual, predicted))


# summarize model performance
def summarize_scores(name, scores):
  for config, score in scores.items():
    values = [[(x[0], x[1], x[2]) for x in tupla] for tupla in score]
    values_1 = [sublista[0] for sublista in values]

    histories = [[x[3] for x in tupla] for tupla in score]
    histories_1 = [sublista[0] for sublista in histories]

    preds = [[x[4] for x in tupla] for tupla in score]
    preds_1 = [sublista[0] for sublista in preds]

    real = [[x[5] for x in tupla] for tupla in score]
    real_1 = [sublista[0] for sublista in real]

    print('Config %s' % (config))
    res = pd.DataFrame(values_1, columns=["RMSE", "MAE", "R2"], index = ['Iteración 1', 'Iteración 2'])
    print(res)
    residuals = [real_1[i] - preds_1[i] for i in range(len(preds_1))]
    # print a summary
    scores_m, score_std = mean(values_1, axis=0), std(values_1, axis=0)
    print('%s: %.3f RMSE (+/- %.3f)' % (name, scores_m[0], score_std[0]))
    print('%s: %.3f MAE (+/- %.3f)' % (name, scores_m[1], score_std[1]))
    print('%s: %.3f R2 (+/- %.3f)' % (name, scores_m[2], score_std[2]))

    # Mostramos la distribución de los errores
    boxplot_errors(values_1)
    print('\n')
    # Mostramos la evolución del error en cada modelo
    plot_loss(histories_1)
    print('\n')
    plot_metrics(histories_1)
    print('\n')
    # Mostramos los valores reales con los predichos
    plot_pred_vs_real(real_1, preds_1)
    print('\n')
    # Mostramos los valores reales con los predichos
    residuals_dist(residuals)
    print('\n')
    residuals_vs_pred(residuals, preds_1)