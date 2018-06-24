import xml.etree.ElementTree as ET


def search_flickr_urls_by_text(flickr, params):
    photos = flickr.photos.search(text=params["KEYWORD"],
                                  tags=params["KEYWORD"],
                                  extras='url_s',
                                  per_page=params["NUMBER_OF_PICTURES"])

    found_urls = [photo["url_s"] for photo in photos["photos"]["photo"]]
    return found_urls
