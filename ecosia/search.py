import json
import logging
import urllib.parse
import urllib.request

from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


SUGGESTION_URL = 'https://ac.ecosia.org/autocomplete?mkt=en-us&'
SEARCH_URL = 'https://www.ecosia.org/search?'
ICON_FILE = 'images/icon.png'


def get_results(query):
    suggestions = []
    try:
        url = SUGGESTION_URL + urllib.parse.urlencode({'q': query})
        req = urllib.request.urlopen(url)
        data = req.read()

        encoding = req.info().get_content_charset('utf-8')
        suggestions = json.loads(data.decode(encoding))['suggestions']
    except Exception as e:
        log.error(str(e))

    suggestions = [query] + suggestions
    return [
        ExtensionResultItem(
            icon=ICON_FILE,
            name=suggestion,
            on_enter=OpenUrlAction(
                SEARCH_URL + urllib.parse.urlencode({'q': suggestion}))
        )
        for suggestion in suggestions]


def no_action():
    return [
        ExtensionResultItem(
            icon=ICON_FILE,
            name='No results',
            on_enter=DoNothingAction()
        )
    ]
