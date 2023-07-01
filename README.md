# Question-Answering Con BERT En Español
Resumén:
Este repositorio es una modificación del repositorio https://github.com/codificandobits/Comprension_de_texto_con_BERT y se basa en el modelo 'distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es' de Hugging Face. Siguiendo el video tutorial https://www.youtube.com/watch?v=iPrwWtVl0LM, hemos adaptado y mejorado la implementación original para proporcionar una generación de respuestas mejorada utilizando este modelo pre-entrenado.
El modelo 'distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es' es una versión compacta y optimizada de BERT para el idioma español, que ha sido previamente ajustada para responder preguntas basadas en el conjunto de datos SQuAD en español. 
El repositorio, proporcionamos el código fuente y los recursos necesarios para implementar de forma rapida y efectiva este modelo.
Ya sea que estés desarrollando una aplicación de preguntas y respuestas, un chatbot o cualquier otra aplicación que requiera generación de respuestas precisas, este repositorio te proporcionará una base sólida para comenzar.

Tecnologías utilizadas
- Python 3.10.8: Lenguaje de programación utilizado para implementar el modelo.
- BERT.
Bibliotecas utilizadas
-   transformers: Biblioteca de Hugging Face que proporciona una interfaz sencilla para utilizar modelos de lenguaje pre-entrenados, incluyendo BERT.
-   tensorflow 2.12.0: Biblioteca de aprendizaje automático de código abierto para la implementación de modelos de aprendizaje profundo.
-   pytorch: Biblioteca de aprendizaje automático de código abierto que proporciona una forma eficiente de entrenar modelos de aprendizaje profundo.
-   bs4: Biblioteca para realizar web scraping y manipular documentos HTML.
-   pip: Gestor de paquetes de Python utilizado para instalar las dependencias necesarias.
-   requests: Biblioteca para realizar solicitudes HTTP y trabajar con APIs web.
-   time: Módulo de Python para trabajar con funciones relacionadas con el tiempo.
-    textwrap: Módulo de Python para dar formato y manipular cadenas de texto.

Uso
1. Clona este repositorio en tu máquina local.
2. Ejecuta el archivo main.py para generar respuestas a preguntas basadas en el contexto proporcionado.

Instalación
Para ejecutar este proyecto, se requiere tener instaladas las dependencias, para esto descomentar las siguientes sentencias:
-  instalar_libreria('tensorflow').
-  instalar_libreria('transformers').
-   instalar_libreria('torch').
-   instalar_libreria('bs4').

Se puede probar este proyecto desde el siguiente notebook en Google Colab:
https://colab.research.google.com/drive/1WIFU46c8Ym10jcWS_3FNcx-yAiUn1YwL?usp=sharing

Contacto
Si tienes alguna pregunta o sugerencia, puedes contactarme a través de lucianodavezac@gmail.com.
