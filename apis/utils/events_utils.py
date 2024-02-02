from utils.postgres_operations import add_event, get_all_events, get_events_by_event_name
def save_event(*args):
    add_event(*args)

def get_events():
    get_all_events()

def get_events_by_name(event_name):
    get_events_by_event_name(event_name)