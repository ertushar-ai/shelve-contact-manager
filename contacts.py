import storage

def add_contact(name, phone, email, address):
    if not phone.isdigit():
        return "Invalid phone"
    if "@" not in email:
        return "Invalid email"

    data = {
        "phone": phone,
        "email": email,
        "address": address
    }

    storage.save_contact(name, data)
    return "Contact added"

def view_contacts():
    return storage.get_all_contacts()

def search_contact(name):
    contacts = storage.get_all_contacts()
    if name in contacts:
        return contacts[name]
    return None

def update_contact(name, phone, email, address):
    contacts = storage.get_all_contacts()
    if name not in contacts:
        return "Not found"

    data = {
        "phone": phone,
        "email": email,
        "address": address
    }

    storage.save_contact(name, data)
    return "Updated"

def delete_contact(name):
    if storage.delete_contact(name):
        return "Deleted"
    return "Not found"