import requests
from ..settings import BASE_URL
import json
import logging

logging.debug(BASE_URL)


class TestNoteApi:
    """ This class is used for testing the all apis"""

    def test_create_note(self):
        url = BASE_URL + '/create/note'
        logging.debug(url)
        data = {'title': 'Note Ten', 'description': 'This is ten note', 'color': 'red', 'is_deleted': False,
                'is_archived': False, 'is_trashed': False, 'is_pinned': False, 'is_restored': False, 'label': 2}
        headers = {
            'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2YXIiOiJhZG1pbjFAZ21haWwuY29tIn0.ejuSmxYaxmz4jHtG24Ox7oVTlwePvZfeVVrYVNqV8Bo'}
        request_data = json.dumps(data)
        logging.debug(request_data)
        response = requests.post(url, request_data, headers=headers)
        logging.info("response is:{}".format(response))
        return response.status_code == 200

    def test_read_note(self):
        url = BASE_URL + '/read/note/1'
        headers = {
            'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2YXIiOiJhZG1pbjFAZ21haWwuY29tIn0.ejuSmxYaxmz4jHtG24Ox7oVTlwePvZfeVVrYVNqV8Bo'}
        response = requests.get(url, headers=headers)
        return response.status_code == 200

    def test_delete_note(self):
        url = BASE_URL + '/delete/note/1'
        headers = {
            'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2YXIiOiJhZG1pbjFAZ21haWwuY29tIn0.ejuSmxYaxmz4jHtG24Ox7oVTlwePvZfeVVrYVNqV8Bo'}
        response = requests.delete(url, headers=headers)
        return response.status_code == 200

    def test_update_note(self):
        url = BASE_URL + '/update/note/1'
        data = {'title': 'Note Ten', 'description': 'This is ten note', 'color': 'red', 'is_deleted': False,
                'is_archived': False, 'is_trashed': False, 'is_pinned': False, 'is_restored': False, 'label': 2}
        headers = {
            'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2YXIiOiJhZG1pbjFAZ21haWwuY29tIn0.ejuSmxYaxmz4jHtG24Ox7oVTlwePvZfeVVrYVNqV8Bo'}
        response = requests.put(url, data=data, headers=headers)
        return response.status_code == 200

    def test_list_note(self):
        url = BASE_URL + '/list/note'
        headers = {
            'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2YXIiOiJhZG1pbjFAZ21haWwuY29tIn0.ejuSmxYaxmz4jHtG24Ox7oVTlwePvZfeVVrYVNqV8Bo'}
        response = requests.get(url=url, headers=headers)
        return response.status_code == 200
