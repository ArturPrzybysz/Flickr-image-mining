from src.config import credentials
from src.util.retrieve_parameters import retrieve_arguments
from src.flickr_requests import search_flickr_urls_by_text
import flickrapi
import sys

# 1. Write FLICKR client ----> 10 points
# 2. Put data in sqlite ----> 10 points
# 3. Script should takes 2 parameters: ----> 10 points
# 		1. "keyword" using to find images,
# 		2. Number of images to download,
# 		3. If parameters are not passed to
# 		   program download 100 most recent
# 4. Find and display image that is most red form database ----> 40 points
# 5. Readable, well organised, bug free, secured code ----> 10 points

params = retrieve_arguments(sys.argv)

params["KEYWORD"] = "cat"

api_key = credentials["FLICKR_KEY"]
api_secret = credentials["FLICKR_SECRET"]

flickr = flickrapi.FlickrAPI(api_key=api_key, secret=api_secret, format='parsed-json')
flickr.authenticate_via_browser(perms='read')

found_images_urls = search_flickr_urls_by_text(flickr=flickr, params=params)

# TODO:
#       1. Download images by urls.
#       2. Add finding images if no keyword is given
#       3. setup DB
#       4. add INSERT into DB
#       5.
