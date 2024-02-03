from utils.postgres_operations import addSaleItem, delete_item_with_good_number
def saveSaleItem(*args):
    addSaleItem(*args)

def delete_item(*args):
    delete_item_with_good_number(*args)