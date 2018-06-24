from config import *
from src.util.retrieve_parameters import retrieve_arguments
from src.flickr_requests import search_images_urls_by_text, search_recent_images_urls
import flickrapi
import sys
from src.util.request_image import save_images_to_db
from src.db.db_operations import set_up_and_connect

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

# TODO:
#       1. Download images by urls.
#       2. Add finding images if no keyword is given
#       3. setup DB
#       4. add INSERT into DB
#       5.
