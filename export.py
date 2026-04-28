import zipfile
import os
from datetime import datetime
import storage

def export_contacts():
    contacts = storage.get_all_contacts()

    if len(contacts) == 0:
        return "No contacts"

    folder = "files"
    if not os.path.exists(folder):
        os.mkdir(folder)

    file_list = []

    for name in contacts:
        file_name = folder + "/" + name + ".txt"
        f = open(file_name, "w")

        data = contacts[name]
        f.write("Name: " + name + "\n")
        f.write("Phone: " + data["phone"] + "\n")
        f.write("Email: " + data["email"] + "\n")
        f.write("Address: " + data["address"] + "\n")

        f.close()
        file_list.append(file_name)

    time = datetime.now().strftime("%Y-%m-%d")
    zip_name = "contacts_export_" + time + ".zip"

    zipf = zipfile.ZipFile(zip_name, "w")

    for file in file_list:
        zipf.write(file)

    zipf.close()

    return "Exported: " + zip_name