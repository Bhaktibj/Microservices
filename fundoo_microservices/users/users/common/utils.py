import re
import bcrypt
import jwt
from ...settings import USER_PASSWORD_SECURITY_SALT, JWT_SECRETE_KEY
from .exceptions import InvalidFormat


def phone_number_valid(phone_number):
    """ this method is check phone_number is valid or not"""
    print("===============>", phone_number)
    if bool(re.search(r"^[0-9]{10,}$", phone_number)):
        print(phone_number)
        return phone_number
    else:
        raise Exception("Invalid phone number format or phone number is None")


def email_validation(email):
    """ this method is used for validate the email"""
    if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)):  # email validation like "bhakti@gmail.com"
        return email
    else:
        raise Exception("Invalid email format or email is None ")


def password_validation_and_hashed(password):
    """ This method is used for validate the email format"""
    print("=========================>", password)
    if bool(re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$",
                      password)):  # password validation like Bhakti@123
        hashed_password = hash_password(password=password)
        return hashed_password
    else:
        raise Exception("Password is None or password incorrect format")


def hash_password(password):
    """ This method is used generate the hash password"""
    salt = USER_PASSWORD_SECURITY_SALT.encode()  # convert salt string to bytes
    hashed_password = bcrypt.hashpw((password.encode()), salt)  # generate hash password
    if hashed_password is not None:  # check pass word is none or not
        print("===================================>", hashed_password)
        return hashed_password  # if not none
    else:
        raise InvalidFormat("password is not hashed")  # else None


def create_jwt_token(var):
    """ This method is used to create jwt token"""
    try:
        payload = {'var': var}
        encoded_token = jwt.encode(payload, JWT_SECRETE_KEY, 'HS256').decode('utf-8')
    except:
        return None  # if invalid data return None
    return encoded_token  # return encoded token


def decode_jwt_token(token):
    """ This method is used to decode the jwt token"""
    try:
        decoded_token = jwt.decode(token, JWT_SECRETE_KEY, algorithms=['HS256'])
    except:
        return None  # if invalid data return None
    return decoded_token  # return decode token


