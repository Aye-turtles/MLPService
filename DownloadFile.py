import requests
import os


def download_csv_from_github(file_url: str, save_directory: str):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    save_path = os.path.join(save_directory, os.path.basename(file_url))

    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            return None
        else:
            return f"Error al descargar el archivo: {response.status_code}"
    except Exception as e:
        return f"Excepción al descargar el archivo: {str(e)}"