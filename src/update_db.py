import json
import requests
from bs4 import BeautifulSoup

# Encabezados para la solicitud HTTP
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

# URL del sitio web a scrapear
url = "https://worldproject1901.wixsite.com/website/novelas-activas"

# Diccionario para almacenar las URLs de los archivos
files_url = {}

def main():
    """
    Función principal que actualiza el contenido y guarda los datos en un archivo JSON.
    """
    update_content()
    with open("files_url.json", "w") as file:
        # Guarda los datos en un archivo JSON
        file.write(json.JSONEncoder().encode(files_url))

def update_content():
    """
    Función que obtiene los enlaces y actualiza el diccionario files_url con los datos obtenidos.
    """
    links = get_links()
    i = 0
    for link in links:
        sub_response = requests.get(link["href"], headers=headers)
        sub_soup = BeautifulSoup(sub_response.text, "html.parser")

        # Actualiza el diccionario files_url con los datos obtenidos
        files_url[f"{i}"] = {}
        files_url[f"{i}"]['title'] = sub_soup.find("h1").text
        files_url[f"{i}"]['links'] = {}
        files_url[f"{i}"]['links']['drive'] = {}
        files_url[f"{i}"]['links']['mediafire'] = {}
        is_mediafire_link = False

        drive_id = 0
        mediafire_id = 0

        for a in sub_soup.find_all("a", class_="j7pOnl"):
            url_file = a["href"]
            if is_mediafire_link == True:
                files_url[f"{i}"]['links']['mediafire'][f"{mediafire_id}"] = url_file
                mediafire_id += 1
                is_mediafire_link = False
            else :
                files_url[f"{i}"]['links']['drive'][f"{drive_id}"] = url_file
                drive_id += 1
                is_mediafire_link = True

        i += 1
    print(files_url)

def get_ln_num() -> int:
    """
    Función que obtiene el número de la última novela en el archivo JSON.
    """
    json_path = "files_url.json"
    with open(json_path, "r") as file:
        json_info: dict = json.load(file)
        file.close()
    return int(list(json_info.keys())[-1])

def get_links():
    """
    Función que obtiene los enlaces de la página principal.
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all("a", class_="StylableButton2545352419__root")

if __name__ == "__main__":
    main()