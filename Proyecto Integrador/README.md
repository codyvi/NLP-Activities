# Proyecto Final
## Equipo 1
- David Alonso Cantú Martínez   A00822455
- Federico Alejandro Alcerreca Treviño A01281459
- Luis E. Candelaria Azpilcueta A00816826
- Gloria Maria Campos García A01422345



---

## ¿Qué hace este proyecto? / What does this project do?
Este proyecto hace un analizador de textos para detectar si algun texto obtenido de Reddit o Twitter entra dentro de un comentario depresiovo, esto se hizo usando bert con el wrapper de la liberia de ktrain. De lado, revisamos que es lo que pasaria si usamos bert con textos largos que sobrepasen los 512 tokens de Bert, esto basado en el paper **How to Fine-Tune BERT for Text Classification?**.

This project makes a text analazyer to detect if any text obtained from Reddit or Twitter falls into a depressive comment, this was done using bert with the ktrain library wrapper. On the side, we checked what would happen if we use bert with long texts that exceed 512 Bert tokens, based on the paper **How to Fine-Tune BERT for Text Classification?**.


## ¿Por qué es útil este proyecto? / Why is this project useful?
Este proyecto es útil para poder detectar si algún texto es depresivo y de lado probar que tanto rendimiento nos daría el modelo con textos largos que pasaron por un summarizer.

This project is useful to be able to detect if any text is depressive and also to test how much performance the model would give us with long texts that went through a summarizer.

## ¿Cómo inicializar el proyecto? / How to get started with this project?
Asegurese de contar con los paquetes de **ktrain, pandas, numpy, kaggle, matplotlib** y **tensorflow** instalados en su ambiente de desarrollo de Python.

Todas las dependencias vienen adjuntas en el **requirements.txt**.

Es necesario correr el código desde Google colab, y tener credenciales para las API's de *kaggle*, *twitter*, y *reddit*.

Make sure you have the **ktrain, pandas, numpy, kaggle, matplotlib** and **tensorflow** packages installed in your Python development environment.

All dependencies are attached in the **requirements.txt**.

You need to run the code from Google colab, and have credentials for the *kaggle*, *twitter*, and *reddit* API's.

`$ pip install -r requirements.txt`

`$ jupiter notebook`

---

### Recursos / Resources
- [How to Fine-Tune BERT for Text Classification?](https://arxiv.org/pdf/1905.05583.pdf)
- [Ktrain Documentation](https://github.com/amaiya/ktrain)
- [Ktrain Tutorial](https://nbviewer.jupyter.org/github/amaiya/ktrain/blob/master/tutorials/tutorial-04-text-classification.ipynb)
- [Base de datos de Reddit](https://www.kaggle.com/nikhileswarkomati/suicide-watch)
