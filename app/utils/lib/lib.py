import random
import sys
# sys.path.insert(1, 'D://RIDE360//ride360-server//app//utils//miscellaneous')
# sys.path.append('ride360-server/app/utils/miscellaneous')
# from ....app import bcrypt
# from app.utils.miscellaneous import numbers
# hash password
from miscellaneous.constants import numbers


# def hash_pass(password):
#     hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')
#     return hash_pass

# # Validate hash password


# def validate_pass(password, hashed_password):
#     is_valid = bcrypt.check_password_hash(hashed_password, password)
#     return is_valid


# Generate OTP
def generate_otp(length):
    otp = ''
    for number in range(length):
        ran = random.randint(0, (len(numbers)-1))
        a = str(ran)
        otp += a + ' '
    return otp


print(generate_otp(5))
