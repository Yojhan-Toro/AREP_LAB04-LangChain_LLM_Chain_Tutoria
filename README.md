# AREP LAB 04 — Tutorial de LangChain LLM Chain

Introducción a LangChain con la API de Google Gemini. Este proyecto demuestra los conceptos fundamentales para construir aplicaciones potenciadas por LLMs usando los componentes principales de LangChain: plantillas de prompts, cadenas, parsers de salida y conversaciones multi-turno. Fue desarrollado como parte del curso de Arquitecturas Empresariales (AREP) en la Escuela Colombiana de Ingeniería Julio Garavito.

## Comenzando

Estas instrucciones te permitirán obtener una copia del proyecto en tu máquina local para propósitos de desarrollo y pruebas.

### Prerrequisitos

Necesitas tener instalado lo siguiente:

* Python 3.10 o superior
* pip (gestor de paquetes de Python)
* Una API Key de Google Gemini (gratis en [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey))

```
python --version
pip --version
```

### Instalación

Una serie de pasos que te indican cómo ejecutar un entorno de desarrollo.

**Paso 1 —** Clona el repositorio

```
git clone [https://github.com/TU_USUARIO/AREP_LAB04-LangChain_LLM_Chain_Tutorial.git]
cd AREP_LAB04-LangChain_LLM_Chain_Tutorial
```

**Paso 2 —** Crea y activa un entorno virtual

```
python -m venv venv
venv\Scripts\activate
```

**Paso 3 —** Instala las dependencias requeridas

```
pip install -r requirements.txt
```

**Paso 4 —** Configura las variables de entorno. Copia el archivo de ejemplo y agrega tu API Key

```
cp .env.example .env
```

Edita el archivo `.env` y agrega tu Google Gemini API Key:

```
GOOGLE_API_KEY=tu_api_key_aqui
```

**Paso 5 —** Ejecuta el script principal

```
python src/llm_chain.py
```



## Ejecutando las Pruebas

### Pruebas de Extremo a Extremo

Las pruebas end-to-end verifican que cada demo en el pipeline de LLM chain se ejecuta correctamente y retorna una respuesta válida y no vacía del modelo.

```
python -m pytest tests/ -v
```

### Prueba Demo 1 — Invocación Directa

Verifica que el modelo puede ser invocado directamente con una lista de mensajes y retorna una respuesta de tipo string no vacía.

```
python -m pytest tests/test_llm_chain.py::test_direct_invocation -v
```

### Prueba Demo 2 — Chain

Verifica que la plantilla de prompt, el LLM y el parser de salida se encadenan correctamente y producen una salida de tipo string.

```
python -m pytest tests/test_llm_chain.py::test_prompt_chain -v
```

### Pruebas de Estilo de Código

Este proyecto sigue los estándares de codificación PEP8. Para verificar el estilo del código:

```
pip install pycodestyle
pycodestyle src/
```

Salida esperada (sin errores significa que el código cumple el estándar):

```
(sin salida = todo correcto)
```

## Despliegue

Este proyecto está diseñado para ejecutarse localmente como herramienta educativa. Para usarlo en un entorno de producción:

1. Establece la variable de entorno `GOOGLE_API_KEY` directamente en el servidor en lugar de usar un archivo `.env`.
2. Usa un servidor WSGI de nivel productivo si expones el chatbot mediante una interfaz web.
3. Nunca subas tu archivo `.env` ni expongas tu API Key en el código fuente.

## Construido Con

* [LangChain](https://python.langchain.com/) - Framework para construir aplicaciones potenciadas por LLMs
* [Google Gemini](https://ai.google.dev/) - Modelo de lenguaje grande usado para generación de texto
* [langchain-google-genai](https://pypi.org/project/langchain-google-genai/) - Integración de LangChain con Google Generative AI
* [python-dotenv](https://pypi.org/project/python-dotenv/) - Gestión de variables de entorno


## Versionado

Usamos **SemVer** para el versionado. Para las versiones disponibles, mira los **tags en este repositorio**.

## Autores

**Yojhan Toro Rivera** 



## Reconocimientos

* [Documentación de LangChain](https://python.langchain.com/docs/) - Referencia principal para construir cadenas
* [Google AI Studio](https://aistudio.google.com/) - Acceso gratuito a la API de Gemini
* Escuela Colombiana de Ingeniería Julio Garavito - Curso AREP
