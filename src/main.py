import update_db
import json

def main():
    json_path = "files_url.json"

    with open(json_path, "r") as file:
        json_info: dict = json.load(file)
        file.close()

    for i in range(update_db.get_ln_num() + 1):
        title = json_info[str(i)]['title']
        print(f"{i}: {title}")

    ln = int(input("Choose a novel: "))
    if ln > update_db.get_ln_num():
        print("Invalid number")
        return
    print("-----------------------------------------------------------")
    print("Title: {}".format(json_info[f"{ln}"]['title']))
    for i in range(int(list(json_info[f"{ln}"]['links']['drive'].keys())[-1]) + 1):
        links = json_info[f"{ln}"]['links']['drive'][f"{i}"]
        print(f"Drive {i}: {links}")

if __name__ == "__main__":
    main()
