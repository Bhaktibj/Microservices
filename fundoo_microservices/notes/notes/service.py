from nameko.rpc import rpc
from .common.db_operations import *
from .models import Notes, Labels
from .config.cache_connection import CacheService
from .common.utils import *

cache = CacheService()


class NoteService(object):
    """ This class is used to create  the services """
    name = 'noteService'

    @rpc
    def create_note_service(self, request_data):
        """ This method is used to create note"""
        if request_data.get('title') and request_data.get('description') and request_data.get('created_by') and \
                request_data.get('label') is not None:
            note = Notes(title=request_data.get('title'),
                         description=request_data.get('description'),
                         color=request_data.get('color'),
                         is_trashed=request_data.get('is_trashed'),
                         is_archived=request_data.get('is_archived'),
                         is_deleted=request_data.get('is_deleted'),
                         is_pinned=request_data.get('is_pinned'),
                         is_restored=request_data.get('is_restored'),
                         created_by=request_data.get('created_by'),
                         label_id=request_data.get('label'))
            save(note)
            return {"message": "successfully created note"}
        else:
            return {"message": "All values are required"}

    @rpc
    def read_note_service(self, request):
        """ this service is used to read the note"""
        if request.get('id') is not None:
            print(request)
            note = filter_by_id(table=Notes, id=request.get('id'))
            if note:
                json_data = serialize_data(object=note)
                print(json_data)
                return {'message': 'read note successfully', 'data': json_data}
            else:
                return {'message': 'note does not exist'}
        else:
            return {'message': 'wrong user note'}

    @rpc
    def delete_note_service(self, request_data):
        """ This service api is used to delete the user note"""
        if request_data.get('id') is not None:
            note = filter_by_id(table=Notes, id=request_data.get('id'))
            if note and note.created_by == request_data.get('created_by'):
                session.query(Notes).filter_by(id=request_data.get('id')).first()
                session.commit()
                session.close()
                return {'message': 'deleted note successfully'}
            else:
                return {'message': 'does not exist note or not deleted'}
        else:
            return {'message': 'wrong user note'}
    @rpc
    def update_note_service(self, request_data, id):
        """ this service  api  is used to update the note"""
        if session.query(Notes).filter_by(id=id).update(request_data):
            session.commit()
            session.close()
            return {'message': 'successfully updated note', 'data': request_data}
        else:
            return {'message': 'does not exist note'}
    @rpc
    def list_note_service(self):
        """ This method is used to list the notes"""
        notes = fetch_all(table=Notes)  # fetch all notes
        if notes:
            json_data = serialize_data(notes)  # serialize the notes
            return {'message':'Successfully list of all notes','data':json_data}
        else:
            return {'message':'something went wrong or'}
    @rpc
    def create_label_service(self, request_data):
        """ This service api is used to create the label """
        if request_data is not None:
            label = Labels(label=request_data.get('label'))
            save(label)
            return {"message": "successfully created labels "}
        else:
            raise KeyError("some values are missing")

    @rpc
    def read_label_service(self, request_data):
        """ This service api is used to read the label"""
        if request_data.get('label_id') is not None:
            label = filter_by_id(table=Labels, id=request_data.get('label_id'))
            if label is not None:
                json_data = serialize_data(object=label)
                return {'message': 'read label successfully {}'.format(json_data)}
            else:
                return {'message': 'label does not exist'}
        else:
            return {'message': 'wrong user note'}

    @rpc
    def update_label_service(self, request_data):
        """ this service  api  is used to update the note"""
        label = filter_by_id(table=Labels, id=request_data.get['label_id'])  # pass the update note id
        if label is not None:
            label.update({Labels.label: request_data.get['label_id']})
            return {'message': 'label updated successfully'}
        else:
            return {'message': 'Does not exist label'}

    @rpc
    def delete_label_service(self, request_data):
        """ This service api is used to delete the label """
        if request_data.get('label_id') is not None:
            label = filter_by_id(table=Labels, id='label_id')
            if label is not None:
                label.delete(synchronize_session=False)
                return {'message': 'deleted label successfully'}
            else:
                return {'message': 'label does not exist'}
        else:
            return {'message': 'something went wrong'}