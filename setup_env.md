# Tutorial para preparar un ambiente de trabajo en Windows

## 1. Instalar Miniconda
Conda es un sistema de gestión de entornos de código abierto especializado en Python. Permite aislar las dependencias de un proyecto a partir de la capa del lenguaje. Utilizar un gestor de entornos y/o otros métodos de aislamiento es una práctica importantísima en programación.

Si bien los entornos aislados a partir de la capa del lenguaje son extensamente usados en investigación y en el prototipado y desarrollo de productos, en la industria suelen usarse mecanismos capaces de aislar capas inferiores. Este es el caso de los extendidos contenedores Docker.

Para instalar Miniconda hay que ir a la [página de descargas del proyecto](https://www.anaconda.com/download?utm_source=anacondadocs&utm_medium=documentation&utm_campaign=download&utm_content=installwindows). Luego, se pueden registrar de manera opcional y descargar el instalador. Una vez en el instalador **es de suma importancia verificar que Conda se instale sin acceso a la variable PATH**. Esta suele ser la opción por defecto, pero pueden ocurrir excepciones.

## 2. Instalar Visual Studio Code
Visual Studio Code es un Entorno de desarrollo integrado (IDE), su rol es facilitar el acceso a proyectos de software gracias a una interfaz gráfica y a un gran número de extensiones creadas por y para programadores. Para instalar VS-Code en Windows basta con ir a la [página de descargas del programa](https://code.visualstudio.com/download), descargar el ejecutable y seguir los pasos del instalador.

## 3. Instalar las extensiones necesarias en VS-code
Una vez instalado Visual Studio Code, podemos instalar las extensiones necesarias para trabajar cómodamente con Python. Para buscar extensiones hay que dirigirse a la barra lateral de VS Code y cliquear sobre el icono que parece una pieza de Tetris. Alternativamente, se puede usar el atajo ```Ctrl+Shift+X```. Luego usamos la barra de búsqueda e instalamos las siguientes extensiones:

- **Jupyter** by Microsoft
- **Jupyter CellTags** by Microsoft
- **Jupyter Keymap** by Microsoft
- **Pylance** by Microsoft
- **Python** by Microsoft
- **Python Debugger** by Microsoft
- **Todo Tree** by Gruntfuggly
- **Excel Viewer** by MESCIUS

## 4. Crear un ambiente Conda
Usando la barra de búsqueda de Windows encontramos la aplicación Miniconda, la abrimos como administrador. ¡Debe abrirse una terminal!  
Luego creamos un nuevo ambiente para el workshop usando el comando:

```bash
conda create -n ML_imputation
```
Seguimos las indicaciones del terminal interactivo, que usualmente nos pedira confirmación para proceder.
## 5. Installar Python 3.10.0
Luego debemos instalar Python dentro del ambiente que acabamos de crear, para esto empezamos entrando en el ambiente con el comando:

```bash
conda activate ML_imputation
```

Luego instalamos Python:

```bash
conda install python=3.10.0
```
En el caso de fallos, podemos especificar un canal mas amplio:

```bash
conda install -c conda-forge python=3.10.0
```
Si los problemas persisten, se puede instalar una versión más flexible:

```bash
conda install python=3.10
```
## 6. Instalar las librerias usando el archivo *requirements.txt*
Finalmente instalamos las librerias necesarias usando el comando:

```bash
pip install -r [path_to_the_requirements.txt]
```

Nuestro ambiente de trabajo esta listo para usar :smile: !