from ..config.create_db import DatabaseService as db

session = db.db_connection()  # create db session


def save(result):
    """ this method is used for save object is table"""
    if result:
        session.add(result)  # save object using session.add() method
        session.commit()  # commmit
        session.close()
        return True  # if save returns True
    else:
        return False  # else False


def filter_by(table, email):
    """ This method is used for filter user by email """
    if session.query(table).filter_by(email=email).first():  # if object is found it returns True
        return email
    else:
        return False  # else it returns false


def filter_by_id(table, id):
    """ This method is  used for filter user by id"""
    result = session.query(table).filter_by(id=id).first()
    if result:
        return result  # if found user
    else:
        return None  # else false


def filter_by_all(self, table, id):
    """ This method is used filter all user detail by user id """
    if self.session.query(table).filter_by(id=id).all():
        return True  # if t it returns True
    else:
        return False  # else false


def update(table, email, password):
    """ This method is used for update the user password"""
    result = filter_by(table=table, email=email)  # search the user
    print(result)
    if result:  # if user
        result.update({table.password: password}, synchronize_session=False)  # update password
        session.commit()
        session.close()
        return True  # if updated return True
    else:
        return False  # else False


def fetch_all(table):
    """ this method is used to fetch the all records  from table"""
    data = session.query(table).all()  # fetch the all data from table
    if data is not None:  # if data is not None
        return data  # return data
    else:
        return None  # else false


def delete_query(table, id):
    """ this method is used for delete the  records from table"""
    result = session.query(table).filter_by(id=id).first()
    if result:  # if object
        result.delete(synchronize_session=False)  # delete the record
        return result  # and return True
    else:
        return False  # otherwise return false
