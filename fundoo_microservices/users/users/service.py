from nameko.rpc import rpc
from .models import User
from .common.exceptions import UserExists, InvalidUserException
from .common.db_operations import *
from .common.utils import *
from .config.cache_connection import CacheService
from .common.send_email import SendMail
from ..settings import HOST_LINK

cache = CacheService()
send = SendMail()


class UserService:
    """ This class is used to create  the services """
    name = 'userService'

    @rpc
    def registration_service(self, request_data):
        """ This method is used to create the registration service"""
        try:
            first_name = request_data.get('first_name')  # get first name from user
            last_name = request_data.get('last_name')  # get last name from user
            email = request_data.get('email')  # email
            password = request_data.get('password')  # get password from user
            phone_number = request_data.get('phone_number')  # get phone_number from user
            print("===================================>", phone_number)
            user_data = filter_by(table=User, email=email)  # check given user email is exists or not
            if not user_data:  # if does not exists user
                user = User(email=email, password=password, first_name=first_name, last_name=last_name,
                            phone_number=phone_number)
                if save(user):  # save user in db
                    encoded_token = create_jwt_token(var=email)  # create jwt token
                    if encoded_token is not None:  # if jwt token and is_active is not None
                        data = f"{HOST_LINK}/activate/{encoded_token}"  # create activation link
                        print(data)
                        send.send_mail(email=email, data=data)  # send activation to user email
            else:
                return {"message": "User already registered , please try with another email"}  # if user exists
            return {"message": '{} Sent registration activation email successfully, please activate'.format(
                request_data.get("email"))}
        except:
            raise Exception("Something went wrong")

    @rpc
    def activate_registration_service(self, request_data):
        """This service is used for user registration activation"""
        try:
            payload = decode_jwt_token(token=request_data.get('token'))  # get payload token
            if payload is not None:
                email = payload.get('var')
                user = session.query(User).filter_by(email=email).first()  # check the user is exists or not
                if user:  # if user and user.is_active is False
                    user.is_active = True  # make it True
                    session.commit()  # commit
                    session.close()  # close
                    return {"message": "confirm registration  successfully"}  # success response
                else:
                    return {"message": "user does not exist"}
            else:
                return {"message": "token is none or invalid"}
        except:
            raise Exception("Something went wrong")



    @rpc
    def login_service(self, request_data):
        """ This service is used to login the user"""
        try:
            email = email_validation(request_data.get('email'))
            password = request_data.get('password')
            if email and password is not None:
                user = session.query(User).filter_by(email=email, password=password_validation_and_hashed(password)).first()
                # check user is exists or not
                if user:  # if user
                    token = create_jwt_token(var=email)  # create jwt_token
                    print(token)
                    cache.set_key(email, token)  # set token into cache
                    return {"message": "login successfully", "data": token}  # login success msge
                else:
                    return {"message": "please enter correct credentials"}  # if not user or credentials wrong
            return {'message':'email and password is required'}
        except:
            raise Exception("something went wrong")

    @rpc
    def forgot_password_service(self, request_data, ):
        """ This service is used to forgot password"""
        email = email_validation(request_data.get('email'))  # get email from user
        if email is not None:  # if email is not None
            user = session.query(User).filter_by(email=email).all()  # check email is exists or not
            if user:  # if exists
                encoded_token = create_jwt_token(var=email)  # create jwt token
                print(encoded_token)
                data = f"{HOST_LINK}/reset/{encoded_token}"
                send.send_mail(email=email, data=data)  # send email forgot password link with payload
                print(data)
                return {"message": "forgot password successfully {}".format(encoded_token)}
            else:
                return {"message": "email does not exists"}
        else:
            raise InvalidUserException("password or email is None or invalid")

    @rpc
    def reset_password_service(self, request_data):
        """ This service is used to reset the password"""
        payload = decode_jwt_token(token=request_data.get('token'))  # get token from payload
        new_password = request_data.get('new_password')  # get new_password from token
        user = session.query(User).filter_by(email=payload.get('var')).first()  # check user is exists or not
        if user:  # if user
            user.password = password_validation_and_hashed(password=new_password)  # set  new_password
            session.commit()  # commit
            session.close()  # close
            return {"message": "Password reset successfully successfully"}
        else:
            return {"message": "user does not exist"}

    @rpc
    def change_password_service(self, request_data):
        """ This service is used to change the password"""
        payload = decode_jwt_token(token=request_data.get('token'))  # get token from payload
        old_password = request_data.get('old_password')  # get old password from user
        new_password = request_data.get('new_password')  # get new_password from token
        user = filter_by(table=User, email=payload.get('var'))  # check user is exists or not
        if user and user.password == password_validation_and_hashed(old_password):  # if user
            user.password = password_validation_and_hashed(password=new_password)  # set  new_password
            session.commit()  # commit
            session.close()  # close
            return {"message": "Password changed successfully successfully"}
        else:
            return {"message": "user does not exist"}
