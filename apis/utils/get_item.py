from .postgres_operations import filter_items_by_category
def get_all_items_in_category(category):
    return filter_items_by_category(category)