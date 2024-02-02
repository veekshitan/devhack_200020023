from .postgres_operations import add_coupon, add_buy_coupon
def save_coupon(roll_no,category):
    return add_coupon(roll_no,category)
def save_buy_coupon(roll_no,category):
    return add_buy_coupon(roll_no,category)