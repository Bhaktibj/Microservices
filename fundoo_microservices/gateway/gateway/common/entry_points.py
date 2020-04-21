from marshmallow import ValidationError
from nameko.exceptions import safe_for_serialization, BadRequest
from nameko.web.handlers import HttpRequestHandler
from .exceptions import InvalidUserException, UserExists, SQLException, InvalidFormat
from .utils import *


class HttpEntrypoint(HttpRequestHandler):  # map errors exceptions
    mapped_errors = {
        BadRequest: (400, 'BAD_REQUEST'),
        ValidationError: (400, 'VALIDATION_ERROR'),
        InvalidUserException: (400, 'InvalidUserException'),
        InvalidFormat: (400, 'InvalidFormat'),
        UserExists: (400, 'UserExists'),
        SQLException: (400, 'SQLException'),

    }

    def response_from_exception(self, exception):  # exception
        """ This method is used for get response from exception"""
        status_code, error_code = 500, 'UNEXPECTED_ERROR'   # if unexpected error

        if isinstance(exception, self.expected_exceptions):  # is instance of exception type
            if type(exception) in self.mapped_errors:  # mapped errors
                status_code, error_code = self.mapped_errors[type(exception)]  # mapped status code 200 expected
            else:
                status_code = 400   # else status code 400
                error_code = 'BAD_REQUEST' # bad request
        return json_response(data=dict(), message=safe_for_serialization(exception), status=status_code)


http = HttpEntrypoint.decorator
