from nameko.standalone.rpc import ClusterRpcProxy
from flask import request
from settings import HOST_CONFIG
from .common.utils import decode_jwt_token, preprocess_request
from flasgger import swag_from
from api import app


@app.route('/login/user', methods=['POST'])
@swag_from('swagger/user_swagger.yaml')
def login():
    """This flask_service is used create the login flask_service"""
    app.logger.debug(request)
    request_data = preprocess_request(request)  # convert request into dict
    with ClusterRpcProxy(HOST_CONFIG) as rpc:  # using cluster rpc
        result = rpc.userService.login_service(request_data)  # call the login service
    return {'response': result}  # return response


@app.route('/register/user', methods=['POST'])
@swag_from('swagger/user_swagger.yaml')
def register():
    """ This flask_service is used to register the user"""
    request_data = preprocess_request(request)  # convert request into dictionary
    print(request_data)
    with ClusterRpcProxy(HOST_CONFIG) as rpc:  # using cluster rpc
        result = rpc.userService.registration_service(request_data)  # call the registration service
    return {'response': result}  # return response


@app.route('/activate/<token>', methods=['GET'])
@swag_from('swagger/user_swagger.yaml')
def activate(token):
    """ This flask_service is used to activate the user registration"""
    request_data = {'token': token}  # token in dict
    with ClusterRpcProxy(HOST_CONFIG) as rpc:
        result = rpc.userService.activate_registration_service(request_data)  # call activate registration service
    return {'response': result}  # return service


@app.route('/forgot/password', methods=['POST'])
@swag_from('swagger/user_swagger.yaml')
def forgot():
    """ This flask_service is used to forgot password"""
    request_data = preprocess_request(request)  # pre process request
    with ClusterRpcProxy(HOST_CONFIG) as rpc:
        result = rpc.userService.forgot_password_service(request_data)  # call forgot password service
    return {'response': result}  # return response


@app.route('/reset/<string:token>', methods=['PUT'])
@swag_from('swagger/user_swagger.yaml')
def reset(token):
    """ This flask_service is used to reset the password"""
    request_data = preprocess_request(request)  # pre- process request
    request_data['token'] = token  # add token in request data
    with ClusterRpcProxy(HOST_CONFIG) as rpc:
        result = rpc.userService.reset_password_service(request_data)  # call the reset password service
    return {'response': result}  # return response


@app.route('/create/note', methods=['POST'])
@swag_from('swagger/note_swagger.yaml')
def create_note():
    """This method is used to create the note"""
    request_data = preprocess_request(request)  # convert request into dictionary
    token = request.headers['token']  # get token from header
    payload = decode_jwt_token(token)  # decode token
    request_data['created_by'] = payload.get('var')  # pass create id to user
    with ClusterRpcProxy(HOST_CONFIG) as rpc:  # using cluster config
        result = rpc.noteService.create_note_service(request_data)  # pass to service
        return {'response': result}  # return response


@app.route('/delete/note/<int:pk>', methods=['DELETE'])
@swag_from('swagger/note_swagger.yaml')
def delete(pk):
    """ This flask_service is used to delete the note"""
    token = request.headers['token']  # request the token from header
    if token is None:  # check token is None or not
        payload = decode_jwt_token(token)  # decode token
        request_data = {'created_by': payload.get('var'), 'id': pk}  # add created_by and id in request data
        with ClusterRpcProxy(HOST_CONFIG) as rpc:  # using cluster rpc
            result = rpc.noteService.delete_note_service(request_data)  # call delete note service flask_service
        return {'response': result}  # return result
    return {'response': 'token is None'}


@app.route('/read/note/<int:pk>', methods=['GET'])
@swag_from('swagger/note_swagger.yaml')
def read_note(pk):
    """ This method is used to read the notes"""
    app.logger.info(request)
    request_data = {'id': pk}
    with ClusterRpcProxy(HOST_CONFIG) as rpc:
        app.logger.debug(rpc)
        result = rpc.noteService.read_note_service(request_data)  # call read activate service
        return {'response': result}  # return response


@app.route('/update/note/<int:pk>', methods=['PUT'])
@swag_from('swagger/note_swagger.yaml')
def put(pk):
    app.logger.info(request)
    request_data = preprocess_request(request)  # convert request into dict
    token = request.headers['token']  # get token from request headers
    payload = decode_jwt_token(token)  # decode token and get payload
    request_data['created_by'] = payload.get('var')  # get created_by token
    with ClusterRpcProxy(HOST_CONFIG) as rpc:
        app.logger.debug(rpc)
        result = rpc.noteService.update_note_service(request_data, pk)  # call the update note service
    return {'response': result}  # return response


@app.route('/list/note', methods=['GET'])
@swag_from('swagger/note_swagger.yaml')
def list_note():
    """ This flask_service is used to list of notes"""
    with ClusterRpcProxy(HOST_CONFIG) as rpc:
        result = rpc.noteService.list_note_service()  # call teh list note service
        return {'response': result}  # return the response


@app.route('/create/label', methods=['POST'])
@swag_from('swagger/label_swagger.yaml')
def create_label():
    """This flask_service is used to create the label"""
    request_data = preprocess_request(request)  # convert request into dict
    with ClusterRpcProxy(HOST_CONFIG) as rpc:
        result = rpc.noteService.create_label_service(request_data)  # call teh create label service
        return {'response': result}  # return the response


@app.route('/read/label/<int:pk>', methods=['GET'])
@swag_from('swagger/label_swagger.yaml')
def read_label(pk):
    """ This method is used to read the label"""
    request_data = {'id': pk}
    with ClusterRpcProxy(HOST_CONFIG) as rpc:
        result = rpc.noteService.read_label_service(request_data)  # call read activate service
        return {'response': result}  # return response


@app.route('/delete/label/<int:pk>', methods=['DELETE'])
@swag_from('swagger/label_swagger.yaml')
def delete_label(pk):
    """ This method is used to read the label"""
    request_data = {'id': pk}
    with ClusterRpcProxy(HOST_CONFIG) as rpc:
        result = rpc.noteService.delete_label_service(request_data)  # call label delete service
        return {'response': result}  # return response


@app.route('/update/label/<int:pk>', methods=['PUT'])
@swag_from('swagger/label_swagger.yaml')
def update_label(pk):
    """ This method is used to read the label"""
    request_data = preprocess_request(request)  # convert request into dict
    with ClusterRpcProxy(HOST_CONFIG) as rpc:
        result = rpc.noteService.update_label_service(request_data, pk)  # call read activate service
    return {'response': result}  # return response
