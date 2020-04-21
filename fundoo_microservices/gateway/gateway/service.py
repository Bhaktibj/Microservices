from nameko.rpc import RpcProxy
from .common.entry_points import http
from .common.exceptions import InvalidUserException, UserExists, InvalidFormat
from .common.utils import *
from .auth.decorator import is_authenticated


class GatewayService:
    name = 'gateway'
    note_rpc = RpcProxy('noteService')
    user_rpc = RpcProxy('userService')

    @http('POST', '/register', expected_exceptions=(InvalidUserException, UserExists, InvalidFormat))
    @preprocess_request
    def registration(self, request):
        result = self.user_rpc.registration_service(request)
        return json_response(data=dict(), message=result.get("message"), status=200)

    @http('GET', '/activate/<string:token>')
    def activate_registration(self, request, **kwargs):
        request_data = {"token": kwargs.get("token")}
        result = self.user_rpc.activate_registration_service(request_data)
        return json_response(data=dict(), message=result.get("message"), status=200)

    @http('POST', '/login', expected_exceptions=(InvalidUserException, UserExists))
    @preprocess_request
    def login(self, request):
        result = self.user_rpc.login_service(request)
        return json_response(data=result, message=result.get("message"), status=200)

    @http('POST', '/forgot', expected_exceptions=(InvalidUserException, UserExists))
    @preprocess_request
    def forgot(self, request):
        result = self.user_rpc.forgot_password_service(request)
        return json_response(data=dict(), message=result.get("message"), status=200)

    @http('POST', '/reset/<string:token>')
    def reset_password(self, request, **kwargs):
        request_data = json_data(request=request)
        request_data['token'] = kwargs.get('token')
        result = self.user_rpc.reset_password_service(request_data)
        return json_response(data=dict(), message=result.get("message"), status=200)

    @http('POST', '/change_password')
    @preprocess_request
    def change_password(self, request):
        request_data = json_data(request=request)
        request_data['token'] = request.headers['token']
        result = self.user_rpc.change_password_service(request_data)
        return json_response(data=request, message=result.get("message"), status=200)

    @http('POST', '/create/note', expected_exceptions=InvalidUserException)
    @is_authenticated
    def create_note(self, request):
        request_data = json_data(request=request)
        token = request.headers['token']
        payload = decode_jwt_token(token)
        request_data['created_by'] = payload.get('var')
        result = self.note_rpc.create_note_service(request_data)
        return json_response(data=result.get("data"), message=result.get("message"), status=200)

    @http('GET', '/read/note/<string:pk>', expected_exceptions=InvalidUserException)
    @is_authenticated
    def read_note(self, request, **kwargs):
        request_data = {'id': kwargs.get('pk')}
        result = self.note_rpc.read_note_service(request_data)
        return json_response(data=result.get("data"), message=result.get("message"), status=200)

    @http('DELETE', '/delete/note/<string:pk>', expected_exceptions=InvalidUserException)
    @is_authenticated
    def delete_note(self, request, **kwargs):
        token = request.headers['token']
        payload = decode_jwt_token(token)
        request_data = {'created_by': payload.get('var'), 'note_id': kwargs.get('pk')}
        result = self.note_rpc.delete_note_service(request_data)
        return json_response(data=result.get("data"), message=result.get("message"), status=200)

    @http('PUT', '/update/note/<string:pk>')
    @is_authenticated
    def update_note(self, request, **kwargs):
        request_data = json_data(request=request)
        token = request.headers['token']
        payload = decode_jwt_token(token)
        request_data['created_by'] = payload.get('var')
        id = kwargs.get('pk')
        result = self.note_rpc.update_note_service(request_data, id)
        return json_response(data=result.get("data"), message=result.get("message"), status=200)

    @http('GET', '/list/note')
    def list_note(self):
        result = self.note_rpc.list_note_service()
        return json_response(data=result.get("data"), message=result.get("message"), status=200)

    @http('POST', '/create/label', expected_exceptions=InvalidUserException)
    @is_authenticated
    @preprocess_request
    def create_label(self, request):
        result = self.note_rpc.create_label_service(request)
        return json_response(data=dict(), message=result.get("message"), status=200)

    @http('GET', '/read/label/<string:pk>', expected_exceptions=InvalidUserException)
    @is_authenticated
    def read_label(self, request, **kwargs):
        request_data = {'id': kwargs.get('pk')}
        result = self.note_rpc.read_label_service(request_data)
        return json_response(data=result.get("data"), message=result.get("message"), status=200)

    @http('DELETE', '/delete/label/<string:pk>', expected_exceptions=InvalidUserException)
    @is_authenticated
    def delete_label(self, request, **kwargs):
        request_data = {'id': kwargs.get('pk')}
        result = self.note_rpc.delete_note_service(request_data)
        return json_response(data=result.get("data"), message=result.get("message"), status=200)

    @http('PUT', '/update/label/<string:pk>', expected_exceptions=InvalidUserException)
    @is_authenticated
    def update_label(self, request, **kwargs):
        request_data = {'id': kwargs.get('pk')}
        result = self.note_rpc.update_note_service(request_data)
        return json_response(data=result.get("data"), message=result.get("message"), status=200)
