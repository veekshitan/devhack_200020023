from utils.postgres_operations import add_event, get_all_events, get_events_by_event_name, delete_event_by_name_and_rollno
def save_event(*args):
    add_event(*args)

def get_events():
    return get_all_events()

def get_events_by_name(event_name):
    return get_events_by_event_name(event_name)

def delete_event(roll_no, name):
    return delete_event_by_name_and_rollno(roll_no, name)