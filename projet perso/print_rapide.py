import aiohttp
import asyncio
import json
import os
import logging
from PyPDF2 import PdfMerger
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Constantes
LIZMAP_PRINT_URL = "https://www.geo70.fr/index.php/lizmap/service?repository=rep8&project=VHauto"
MAP_URL = "https://www.geo70.fr/index.php/view/map?repository=rep8&project=VHauto"
USERNAME = "DSTT"
PASSWORD = "%Dstt70"
PRINT_FOLDER = "config/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")

# Configuration du logging
logging.basicConfig(filename="vh.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Création des dossiers de sortie en fonction de la date actuelle
def create_folders(date_format="%d-%m-%Y"):
    current_date = datetime.now().strftime(date_format)
    folder_name = f"VH_{current_date}"
    output_folder = os.path.join(os.getcwd(), folder_name)
    individual_maps_folder = os.path.join(output_folder, "cartes individuelles")

    for folder in [output_folder, individual_maps_folder]:
        os.makedirs(folder, exist_ok=True)

    return output_folder, individual_maps_folder

# Téléchargement d'un PDF à partir de LizMap, du cookie et d'un fichier de config
async def download_pdf(session, json_file, headers, print_folder, individual_maps_folder):
    pdf_file = os.path.splitext(json_file)[0] + ".pdf"
    json_file_path = os.path.join(print_folder, json_file)

    if not os.path.exists(json_file_path):
        logging.error(f"Fichier JSON manquant : '{json_file}'")
        return None, None

    with open(json_file_path, 'r', encoding='utf-8') as json_data_file:
        json_data = json.load(json_data_file)
        try:
            async with session.post(LIZMAP_PRINT_URL, headers=headers, data=json_data) as response:
                response.raise_for_status()  # Gestion des erreurs HTTP
                pdf_data = await response.read()
                pdf_file_path = os.path.join(individual_maps_folder, pdf_file)
                with open(pdf_file_path, "wb") as pdf_data_file:
                    pdf_data_file.write(pdf_data)
                print(f"PDF sauvegardé en tant que '{pdf_file}'")
                logging.info(f"PDF sauvegardé en tant que '{pdf_file}' pour le fichier JSON '{json_file}'")
                return pdf_file, pdf_file_path
        except aiohttp.ClientResponseError as e:
            logging.error(f"Échec de la requête pour le fichier JSON '{json_file}': {e}")
            return None, None

# Téléchargement de tous les PDF en parallèle
async def download_all_pdfs(output_folder, headers, print_folder, individual_maps_folder):
    print("\nTéléchargement des PDFs...")
    async with aiohttp.ClientSession() as session:
        files_to_download = [json_file for json_file in os.listdir(print_folder) if json_file.endswith(".json")]
        tasks = [download_pdf(session, json_file, headers, print_folder, individual_maps_folder) for json_file in files_to_download]
        return await asyncio.gather(*tasks)

# Fusion des PDF en deux fichiers en parallèle
async def merge_pdfs_async(output_folder, current_date, pdf_list):
    print("\nFusion des PDFs...")
    pict_pdf = PdfMerger()
    other_pdf = PdfMerger()

    pdf_list = [(pdf_file, pdf_path) for pdf_file, pdf_path in pdf_list if pdf_file and pdf_path]
    pdf_list.sort(key=lambda x: x[0])

    for pdf_file, pdf_path in pdf_list:
        if pdf_file.endswith("pict.pdf"):
            pict_pdf.append(pdf_path)
        else:
            other_pdf.append(pdf_path)

    pict_merged_pdf = f"vh_avec_pictogrammes_{current_date}.pdf"
    other_merged_pdf = f"vh_{current_date}.pdf"

    pict_pdf.write(os.path.join(output_folder, pict_merged_pdf))
    other_pdf.write(os.path.join(output_folder, other_merged_pdf))

    logging.info(f"Fusion des PDFs avec pictogrammes dans '{pict_merged_pdf}'")
    logging.info(f"Fusion des autres PDFs dans '{other_merged_pdf}'")
    print(f"\nLes PDFs fusionnés ont été créés dans le dossier '{output_folder}'")
    logging.info(f"Les PDFs fusionnés ont été créés dans le dossier '{output_folder}'")

# Obtiention des cookies via le navigateur
def get_cookies_via_browser(url, username, password):
    try:
        with webdriver.Chrome(options=chrome_options) as driver:
            driver.get(url)
            os.system('clear' if os.name == 'posix' else 'cls')
            print("\nConnexion à HSN...")
            driver.find_element(By.NAME, "auth_login").send_keys(username)
            driver.find_element(By.NAME, "auth_password").send_keys(password, Keys.RETURN)
            cookies = driver.get_cookies()

        cookies_string = '; '.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
        return cookies_string

    except Exception as e:
        logging.error(f"Erreur lors de l'obtention des cookies : {e}")
        return None

if __name__ == "__main__":
    headers = {"Cookie": get_cookies_via_browser(MAP_URL, USERNAME, PASSWORD)}
    output_folder, individual_maps_folder = create_folders()
    pdf_list = asyncio.run(download_all_pdfs(output_folder, headers, PRINT_FOLDER, individual_maps_folder))
    asyncio.run(merge_pdfs_async(output_folder, datetime.now().strftime("%d-%m-%Y"), pdf_list))