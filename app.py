from config import *
from src.util.retrieve_parameters import retrieve_arguments
from src.flickr_requests import search_images_urls_by_text, search_recent_images_urls
import flickrapi
import sys
from src.util.request_image import save_images_to_db
from src.db.db_operations import set_up_and_connect, find_the_most_red_image
from PIL import Image
from io import BytesIO

db_connection = set_up_and_connect()

api_key = FLICKR_KEY
api_secret = FLICKR_SECRET

flickr = flickrapi.FlickrAPI(api_key=api_key, secret=api_secret, format='parsed-json')
flickr.authenticate_via_browser(perms='read')

params = retrieve_arguments(sys.argv)
image_urls = []
if params is None:
    image_urls = search_recent_images_urls(flickr=flickr)
else:
    image_urls = search_images_urls_by_text(flickr=flickr, params=params)

save_images_to_db(image_urls, db_connection)

image_data = find_the_most_red_image(db_connection)
image = Image.open(BytesIO(image_data[0]))
image.show()

print("Sredni poziom R w najbardziej czerwonym obrazie:", image_data[1])
