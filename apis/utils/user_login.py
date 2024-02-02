from utils.postgres_operations import find_user
def user_verification(roll_number,password):
    if not roll_number or not password:return False
    if find_user(roll_number, password):
        return True
    return False