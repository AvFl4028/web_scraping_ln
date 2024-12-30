import json
import update_db

def main():
    """
    Función principal que muestra las novelas disponibles y permite al usuario elegir una para ver sus enlaces.
    """
    # Cargar la información del archivo JSON
    with open("files_url.json", "r") as file:
        json_info = json.load(file)

    # Mostrar la lista de novelas disponibles
    for i in range(update_db.get_ln_num() + 1):
        title = json_info[str(i)]['title']
        print(f"{i}: {title}")

    # Solicitar al usuario que elija una novela
    ln = int(input("Choose a novel: "))
    if ln > update_db.get_ln_num():
        print("Invalid number")
        return

    # Mostrar los detalles de la novela seleccionada
    print("-----------------------------------------------------------")
    print("Title: {}".format(json_info[f"{ln}"]['title']))
    for i in range(int(list(json_info[f"{ln}"]['links']['drive'].keys())[-1]) + 1):
        links = json_info[f"{ln}"]['links']['drive'][f"{i}"]
        print(f"Drive {i}: {links}")

if __name__ == "__main__":
    main()
