from requests import get
import os
from config import ROOT_DIR
from PIL import Image
import numpy as np
from src.db.db_operations import insert_image_entity


def save_images_to_db(urls: [str], db_connection):
    temporary_file_address = os.path.join(ROOT_DIR, "tmp.img")
    for url in urls:
        response = get(url)
        if response.status_code == 200:
            with open(temporary_file_address, 'wb') as f:
                f.write(response.content)
                image = Image.open(open(temporary_file_address, 'rb'))
                red, green, blue = _calculate_average_colors(image)

                insert_image_entity(db_connection=db_connection,
                                    image_blob=response.content,
                                    url=url,
                                    avg_red_lvl=red,
                                    avg_green_lvl=green,
                                    avg_blue_lvl=blue)
        else:
            print("Failed to download image: ", url)
            os.remove(temporary_file_address)


def _calculate_average_colors(image: Image):
    return np.array(image).mean(axis=(0, 1))
