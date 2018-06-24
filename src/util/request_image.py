from requests import get
from PIL import Image
import numpy as np
from src.db.db_operations import insert_image_entity
from io import BytesIO


def save_images_to_db(urls: [str], db_connection):
    for url in urls:
        response = get(url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            red, green, blue = _calculate_average_colors(image)
            insert_image_entity(db_connection=db_connection,
                                image_blob=response.content,
                                url=url,
                                avg_red_lvl=red,
                                avg_green_lvl=green,
                                avg_blue_lvl=blue)
        else:
            print("Failed to download image: ", url)


def _calculate_average_colors(image: Image):
    return np.array(image).mean(axis=(0, 1))
