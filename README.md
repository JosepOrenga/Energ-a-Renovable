# Energia Renovable

Este proyecto tiene como propósito comparar diferentes modelos predictivos sobre la potencia de energía eléctrica generada por una planta solar fotovoltaica y un parque eólico. Con la finalidad de desarrollar una herramienta con la que una empresa generadora de energía renovable sea capaz de ofrecer ofertas de venta de energía precisas en el mercado intradiario de subastas español.

En base a la bibliografía revisada, las Redes Neuronales Recurrentes (RNNs) y las Redes Neuronales Convolucionales (CNNs), se presentan como una alternativa muy prometedora para la predicción de las series temporales. De esta manera, se analizan los resultados que se obtienen al comparar diferentes modelos basados en las arquitecturas mencionadas.

Los resultados obtenidos demuestran que la arquitectura CNN es la que mejores predicciones obtiene para la energía fotovoltaica, mientras que, pese a presentar un alto coste computacional la arquitectura Stacked LSTM es la más precisa para la energía eólica.

No obstante, no se ha obtenido unos resultados satisfactorios, puesto que, la precisión de los modelos no es la esperada. En consecuencia, se propone estudiar el comportamiento de los modelos con longitud de datos de entrada mayor, con la intención de aumentar la precisión de los resultados. Sin embargo, esta mejora no se ha implementado debido al alto coste computacional que conlleva.
