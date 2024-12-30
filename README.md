# Proyecto Get_LN

Este proyecto tiene como objetivo scrapear un sitio web para obtener enlaces de novelas ligeras y almacenarlos en un archivo JSON. Luego, permite al usuario seleccionar una novela y ver los enlaces disponibles.

## Requisitos

- Python 3.x
- Librerías: `requests`, `beautifulsoup4`

Puedes instalar las librerías necesarias ejecutando:
```bash
pip install -r requirements.txt
```

## Archivos
```update_db.py```
Este archivo contiene las funciones necesarias para scrapear el sitio web y actualizar el archivo JSON con los enlaces de las novelas.

```main()```: Función principal que actualiza el contenido y guarda los datos en un archivo JSON.

```update_content()```: Función que obtiene los enlaces y actualiza el diccionario files_url con los datos obtenidos.

```get_ln_num() -> int```: Función que obtiene el número de la última novela en el archivo JSON.

```get_links()```: Función que obtiene los enlaces de la página principal.

```main.py```
Este archivo contiene la lógica para mostrar las novelas disponibles y permitir al usuario seleccionar una para ver sus enlaces.

```main()```: Función principal que muestra las novelas disponibles y permite al usuario elegir una para ver sus enlaces.
### Uso
Ejecuta update_db.py para scrapear el sitio web y actualizar el archivo JSON con los enlaces de las novelas:
```bash
python update_db.py
```
Ejecuta ```main.py``` para mostrar las novelas disponibles y permitir al usuario seleccionar una para ver sus enlaces:
```bash
python main.py
```
## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.
