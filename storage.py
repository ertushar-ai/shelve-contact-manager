import shelve

DB_NAME = "contacts_db"

def get_all_contacts():
    db = shelve.open(DB_NAME)
    data = dict(db)
    db.close()
    return data

def save_contact(name, data):
    db = shelve.open(DB_NAME)
    db[name] = data
    db.close()

def delete_contact(name):
    db = shelve.open(DB_NAME)
    if name in db:
        del db[name]
        db.close()
        return True
    db.close()
    return False