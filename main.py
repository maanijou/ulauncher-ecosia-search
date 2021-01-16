from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from ecosia.search import get_results, no_action
from ecosia.counter import get_trees_count


class EcosiaSearchExtension(Extension):
    def __init__(self):
        super(EcosiaSearchExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()
        if len(query.strip()) == 0:
            return RenderResultListAction(no_action())
        else:
            if query.strip() == '#count':
                count = get_trees_count()
            return RenderResultListAction(count + get_results(query))


if __name__ == '__main__':
    EcosiaSearchExtension().run()
