# GUI - YT DOWNLOADER  

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)


Interfaz gráfica sencilla para Windows. Permite descargar vídeos de YouTube a partir del link de un vídeo.

## ÍNDICE

 - [Demo](#demo)
 - [Requisitos](#requisitos)
 - [Para empezar](#para-empezar) 
 - [Personalizar](#personalizar)
 - [Nota](#nota)

## DEMO

<details>
  <summary>Ver</summary>

  ![demo](https://github.com/user-attachments/assets/3e1c7fb2-01e2-4eb8-9f6d-85c7b9d81fde)
  
</details>



## REQUISITOS

**Python:** [3.8.10](https://www.python.org/downloads/release/python-3810/) (Versión usada para este proyecto.)

**Paquetes:** (Versiones usadas en este proyecto) 
 - certifi==2024.7.4
 - charset-normalizer==3.3.2
 - idna==3.7
 - pillow==10.4.0
 - pytubefix==6.13.0
 - requests==2.32.3
 - urllib3==2.2.2


## PARA EMPEZAR
<details>
<summary>Entorno virtual</summary>

Te recomiendo utilizar un [entorno virtual](https://docs.python.org/es/3/tutorial/venv.html) al trabajar con este proyecto, para evitar posibles conflictos en otros proyectos de Python.
Puedes crearlo de la siguiente manera:

En la terminal, deberás ubicarte en la carpeta donde quieras crear tu entorno (Recuerda la ubicación para su uso futuro)
```bash
 # En mi caso lo haré en la carpeta escritorio.
 c:\users\admin\escritorio>
```
Ejecuta el siguiente comando en donde deberás escribir el nombre para tu entorno al final
```bash
 # Puedes reemplazar "mi-entorno-virtual" por el nombre para tu entorno.
 c:\users\admin\escritorio>python -m venv mi-entorno-virtual
```
Ahora, tendrás que activar tu entorno para poder trabajar sin inconvenientes con este proyecto.
Ejecuta el siguiente comando para activar tu entorno
```bash
 # Reemplaza el inicio por el nombre de tu entorno
 c:\users\admin\escritorio>mi-entorno-virtual\Scripts\activate
```
Listo, ahora puedes instalar los paquetes necesarios.

Si necesitas desactivarlo, puedes hacerlo de la siguiente manera:
```bash
 # Ubicarte en la carpeta Scripts de tu entorno
 c:\users\admin\escritorio\mi-entorno-virtual\Scripts>deactivate #Presiona enter
 # De una manera similar a la activación
 c:\users\admin\escritorio>mi-entorno-virtual\Scripts\deactivate
```
</details>

### Instalación

Desde una terminal, deberas de ubicarte dentro de la carpeta principal de este repositorio.

Necesitas instalar los paquetes necesarios para el funcionamiento de este proyecto, puedes hacerlo de la siguiente manera:

Usando [PIP](https://pip.pypa.io/en/stable/getting-started/)

```bash
 #Instalar una lista de paquetes guardada en un archivo.
 pip install -r requirements.txt
```
Ya puedes iniciar la aplicación con el siguiente comando:
```bash
 python app.py
```
Veras la siguiente pantalla:

![Pantall de inicio](https://github.com/user-attachments/assets/88267c92-5c63-4875-bb02-41bd98eae5ee)


Sientete libre de explorar la aplicación.

## PERSONALIZAR

A continuación, se da una breve descripción de como puedes cambiar el aspecto o funcionalidad de este proyecto, siguiendo su estructura.

Estructura del proyecto:

![Estructura del proyecto](https://github.com/user-attachments/assets/39ce3596-1a86-417a-8e00-2daf1dad5648)


<details>
 
 <summary>assets</summary>
 
 - Recursos gráficos a usar dentro de la aplicación, como el ícono, imagenes de fondo, etc.
 
  Agrega tantas imágenes o recursos como necesites en esta carpeta, te recomiendo hacerlo por carpetas de acuerdo a la vista correspondiente.

  ![assets](https://github.com/user-attachments/assets/f4bcb46f-aa3e-4789-9950-741195448b8e)

 
</details>

<details>
 
 <summary>constants</summary>
 
 - Archivos .py con constantes a usar en el proyecto, como colores, URLs, fuentes, etc.
 
 Modifica los archivos existentes agregando tus propias constantes. Usa la función resource_path para agregar rutas de tus recursos de la carpeta assets, guíate de las constantes existentes para hacerlo.

 ![constants](https://github.com/user-attachments/assets/578d566d-67ee-4cc9-9a0e-d0921a354b7c)

 
</details>

<details>
 
 <summary>frames</summary>
 
 - Contiene todas las vistas de la aplicación, dividida por secciones (Pantalla principal, menú, etc)

 En la carpeta panels puedes agregar nuevos directorios que contengan las vistas de cada opción del menú, en caso de añadir nuevas funcionalidades a la aplicación. Por ejemplo, la carpeta downloadvideo contiene las vistas necesarias para todo el proceso de descarga de un vídeo.
Puedes agregar dichas funcionalidades, editando menu.py dentro de la carpeta frames, para mostrar las vistas guardadas en la carpeta panels de a cuerdo a tus nuevas funciones.

![frames](https://github.com/user-attachments/assets/c2085197-b2bc-4644-a1f9-d3fd8c19fb0c)


</details>

<details>
 
 <summary>utils</summary>
 
 - Funciones repetitivas para el uso dentro del proyecto (cargar una imagen, obtener la ruta actual, etc)
 
 Agrega nuevos archivos que engloben las distintas funciones repetitivas que detectes al trabajar, de acuerdo al ambito que pertenezcan. Por ejemplo, en frames.py solo hay funciones referentes al trabajar con frames, como limpiar el contenido de uno.

 ![utils](https://github.com/user-attachments/assets/84399c45-032d-475a-8b05-0c8a3bcad827)


</details>

<details>
 
 <summary>widgets</summary>
 
 - Contiene los widgets personalizados para este proyecto ( botones, etiquetas de: texto, título, imagen, etc)

Modifica o agrega tantos widgets personalizados como lo necesites, puedes cambiar los colores de los existentes, la forma, tamaño etc. En los casos de los botones con imágenes, solo debes de agregar la nueva imagen de fondo del boton en la carpeta assets/btn_images y cambiar el nombre de la ruta del botón en constants/images_paths para visualizar el nuevo aspecto.

![widgets](https://github.com/user-attachments/assets/0f3652ac-72e6-48fe-9896-13a2883e362e)


</details>

## NOTA

Este proyecto fue desarrollado con fines educativos, para la práctica de creación de interfaces gráficas usando Python y tkinter.


