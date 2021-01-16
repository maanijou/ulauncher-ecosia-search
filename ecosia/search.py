import json
import logging
import urllib.parse
import urllib.request

from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

from . import constants

log = logging.getLogger(__name__)
# log.setLevel(logging.DEBUG)


def get_results(query):
    suggestions = []
    try:
        url = constants.SUGGESTION_URL + urllib.parse.urlencode({'q': query})
        req = urllib.request.urlopen(url)
        data = req.read()

        encoding = req.info().get_content_charset('utf-8')
        suggestions = json.loads(data.decode(encoding))['suggestions']
    except Exception as e:
        log.error(str(e))

    suggestions = [query] + suggestions
    return [
        ExtensionResultItem(
            icon=constants.ICON_FILE,
            name=suggestion,
            on_enter=OpenUrlAction(
                constants.SEARCH_URL + urllib.parse.urlencode({'q': suggestion}))
        )
        for suggestion in suggestions]


def no_action():
    return [
        ExtensionResultItem(
            icon=constants.ICON_FILE,
            name='No results',
            on_enter=DoNothingAction()
        )
    ]
