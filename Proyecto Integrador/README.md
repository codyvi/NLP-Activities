# Proyecto Final
## Equipo 1
- David Alonso Cantú Martínez   A00822455
- Federico Alejandro Alcerreca Treviño A01281459
- Luis E. Candelaria Azpilcueta A00816826
- Gloria Maria Campos García A01422345



---

## Arquitectura del Repositorio / Repository Architecture
El proyecto principal esta en el archivo **Modelo Proyecto Final.ipynb**, para poder correr este se necesitan los datos que se encuentran en la carpeta de **Data** dentro de la otra carpeta de **Data and Data Cleaning**. Esta carpeta antes mencionada contiene otras carpetas que contienen los notebooks de limpieza de datos y los archivos .py y notebook de obtención de datos.

The main project is in the **Final Project Model.ipynb** file, in order to run this you need the data that is in the **Data** folder inside the other **Data and Data Cleaning** folder. This aforementioned folder contains other folders containing the data cleaning notebooks and the .py and data fetching notebook files.

## ¿Qué hace este proyecto? / What does this project do?
Este proyecto hace un analizador de textos para detectar si algun texto obtenido de Reddit o Twitter entra dentro de un comentario depresiovo, esto se hizo usando bert con el wrapper de la liberia de ktrain. De lado, revisamos que es lo que pasaria si usamos bert con textos largos que sobrepasen los 512 tokens de Bert, esto basado en el paper **How to Fine-Tune BERT for Text Classification?**.

This project makes a text analazyer to detect if any text obtained from Reddit or Twitter falls into a depressive comment, this was done using bert with the ktrain library wrapper. On the side, we checked what would happen if we use bert with long texts that exceed 512 Bert tokens, based on the paper **How to Fine-Tune BERT for Text Classification?**.


## ¿Por qué es útil este proyecto? / Why is this project useful?
Este proyecto es útil para poder detectar si algún texto es depresivo y de lado probar que tanto rendimiento nos daría el modelo con textos largos que pasaron por un summarizer.

This project is useful to be able to detect if any text is depressive and also to test how much performance the model would give us with long texts that went through a summarizer.

## ¿Cómo inicializar el proyecto? / How to get started with this project?
Asegurese de contar con los paquetes de **ktrain, pandas, numpy, kaggle, matplotlib, tweepy, pymongo, credentials, transformers, seaborn** y **tensorflow** instalados en su ambiente de desarrollo de Python.

Todas las dependencias vienen adjuntas en el **requirements.txt**.

Descargar modelo de bert si se quiere probar de [aqui](https://drive.google.com/drive/folders/1-8795s0Aa8c3DfuAMa3_wX5es35kcPib?usp=sharing).

Es necesario correr el código desde Google colab, y tener credenciales para las API's de *kaggle*, *twitter*, y *reddit*.

Make sure you have the **ktrain, pandas, numpy, kaggle, matplotlib, tweepy, pymongo, credentials, transformers, seaborn** and **tensorflow** packages installed in your Python development environment.

All dependencies are attached in the **requirements.txt**.

Download the bert model if you want to try it from [here](https://drive.google.com/drive/folders/1-8795s0Aa8c3DfuAMa3_wX5es35kcPib?usp=sharing).

You need to run the code from Google colab, and have credentials for the *kaggle*, *twitter*, and *reddit* API's.

`$ pip install -r requirements.txt`

`$ jupiter notebook`

---

### Recursos / Resources
- [How to Fine-Tune BERT for Text Classification?](https://arxiv.org/pdf/1905.05583.pdf)
- [Ktrain Documentation](https://github.com/amaiya/ktrain)
- [Ktrain Tutorial](https://nbviewer.jupyter.org/github/amaiya/ktrain/blob/master/tutorials/tutorial-04-text-classification.ipynb)
- [Base de datos de Reddit](https://www.kaggle.com/nikhileswarkomati/suicide-watch)