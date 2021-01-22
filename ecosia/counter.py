import json
import logging
import urllib.request

from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from . import constants

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def get_trees_count():
    rate = ''
    count = ''
    try:
        req = urllib.request.urlopen(constants.COUNTER_API)
        data = req.read()

        encoding = req.info().get_content_charset('utf-8')
        resp = json.loads(data.decode(encoding))
        count = resp['count']
        rate = resp['rate']
    except Exception as e:
        log.error(str(e))
    if rate:
        return [
            ExtensionResultItem(
                icon=constants.ICON_FILE,
                name=f'{count:,} trees planted with rate: {rate}!',
                on_enter=DoNothingAction()
            )]
    else:
        return []
