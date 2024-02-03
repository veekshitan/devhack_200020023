from .postgres_operations import add_coupon, add_buy_coupon,delete_coupon_with_rollno_and_category
def save_coupon(roll_no,category):
    return add_coupon(roll_no,category)
def save_buy_coupon(roll_no,category):
    return add_buy_coupon(roll_no,category)
def delete_coupon(roll_no, category):
    delete_coupon_with_rollno_and_category(roll_no, category)