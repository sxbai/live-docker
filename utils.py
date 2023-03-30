import xbmcaddon
import os
import re

_ADDON = xbmcaddon.Addon()


def get_image_path(image_filename):
    return os.path.join(_ADDON.getAddonInfo('path'), 'resources', 'images',
                        image_filename)


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def cleanText(src):
    clean = re.sub('[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]', '', src)
    return clean