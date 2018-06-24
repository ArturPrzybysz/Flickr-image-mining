from config import DEFAULT_NUMBER_OF_PICTURES


def search_images_urls_by_text(flickr, params):
    photos = flickr.photos.search(text=params["KEYWORD"],
                                  tags=params["KEYWORD"],
                                  extras='url_s',
                                  per_page=params["NUMBER_OF_PICTURES"],
                                  sort='relevance')

    found_urls = [photo["url_s"] for photo in photos["photos"]["photo"]]
    return found_urls


def search_recent_images_urls(flickr):
    photos = flickr.photos.search(extras='url_s',
                                  per_page=DEFAULT_NUMBER_OF_PICTURES,
                                  sort='date-posted-desc')

    found_urls = [photo["url_s"] for photo in photos["photos"]["photo"]]
    return found_urls
