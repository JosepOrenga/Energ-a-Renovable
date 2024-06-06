# Energia Renovable

En este trabajo, se acomete comparar diferentes modelos predictivos sobre la cantidad de energía eléctrica generada por una planta solar fotovoltaica y un parque eólico, con el fin de desarrollar una herramienta para que una empresa generadora de energía se capaz de ofrecer ofertas de venta en el mercado intradiario español.

En base a estudios anteriores, las Redes Neuronales Recurrentes (RNNs) y las Redes Neuronales Convolucionales (CNNs), se presentan como una alternativa muy prometedora para la predicción de las series temporales. De esta manera, se analizan los resultados que se obtienen al comparar diferentes modelos basados en las arquitecturas anteriores.

Los resultados obtenidos, demuestran como para energía fotovoltaica, la arquitectura CNN es la que mejores resultados obtiene, mientras que, para la energía eólica, pese a representar un alto coste computacional la arquitectura Stacked LSTM, es la mejor precisa.

No obstante, no se puede concluir que se hayan obtenido unos resultados satisfactorios, puesto que, la precisión de los modelos no es la esperada. En consecuencia, se propone estudiar el comportamiento de los modelos con longitud de entrada más larga, para mejorar los resultados. Sin embargo, no se ha podido implementar esta mejora debido al alto coste computacional que conlleva.
