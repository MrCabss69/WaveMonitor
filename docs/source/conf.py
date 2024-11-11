import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Información del proyecto
project = 'Teoría de Ondas y Comunicaciones'
author = 'Tu Nombre'
release = '0.1.0'

# Extensiones
extensions = ['myst_parser', 'sphinx_rtd_theme']

# Configuración del tema HTML
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Tipos de archivos fuente admitidos
source_suffix = ['.rst', '.md']

# Rutas de entrada y salida
master_doc = 'index'
