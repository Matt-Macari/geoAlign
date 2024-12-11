# GeoAlign
Aerial Photograph Georeferencing Software   

*Made for California Polytechnic State University, Humboldt*

## Table of Contents
1. [Description](#description)
2. [Authors](#authors)
3. [Getting Started](#getting-started)
    - [Installing](#installing)
    - [Dependencies](#dependencies)
    - [Virtual Enviroment](#virtual-enviroment)
    - [Executing Program](#executing-program)
4. [Note](#note)

## 1. Description

### What is GeoAlign
GeoAlign is a python based software to automate georeferencing aerial photographs

GeoAligns Purpose is to speed up the time-consuming process of georeferencing historical aerial photographs stored in the Cal Poly Humboldt Library Special Collections Archive.

### GeoAlign is intended to be used by
- Cal Poly Humboldt Library administration and archive specialists
- Faculty from the Department of Environmental Science & Management (ESM)
- Faculty from the Department of Geography, Environment & Spatial Analysis (GES)

## 2. Authors
- [Matthew Marcotullio](https://github.com/MatthewMarcotullio)  
- [Matt Macari](https://github.com/Matt-Macari)  
- [Lily Yassemi](https://github.com/lilyyassemi)  
- [Dylan Lucas](https://github.com/Dylanlucas01)


## 3. Getting Started

### Installing
The source code is available as a public repository 
It can be downloaded at: https://github.com/Matt-Macari/geoAlign

Clone the Repo
```
git clone https://github.com/Matt-Macari/geoAlign.git
```

### Dependencies
- Have python3 installed
- Have gdal installed locally - [how to download gdal](https://mapscaping.com/installing-gdal-for-beginners/)

### Virtual Enviroment

#### Create a Python Virtual Environment
```	
python -m venv env 
```

#### Activate the Python Virtual Environment

##### For Windows
```
.\env\Scripts\activate
```

##### For MacOS
```
source env/bin/activate
```

##### For Linux
```
source env/bin/activate
```

#### Install Local Dependencies for Virtual Enviroment
```
pip install -r requirements.txt
```

### Executing Program

*Make sure your local virtual environment is activated*
- Run GeoAlign
```
python3 src/main.py
```

- Run Unit Test
```
python3 -m unittest discover -s unit -p '*_test.py'
```

## 4. Note
- In `src/main.py` make sure to set train image variable `train_image_path` to relative or absolute path in local directory. 
    -  By default it is set to `'../base.tif'`

- Make sure you activate your local virtual environment every time you work on the project.

- If you name your virtual environment something different than env, please add the path to our .gitignore file.

- If you introduce new dependencies to the project, make sure to add them to the requirements file. 
    - To add dependencies to the requirement file, run the following command:
```            
pip freeze > requirements.txt
```