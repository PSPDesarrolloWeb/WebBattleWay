import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("credentialsFirestore.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

def print_all_users():
    users_ref = db.collection('user')
    users = users_ref.stream()
    for user in users:
        print(f"{user.id} => {user.to_dict()}")
print_all_users()

# def addTournament(name, date):
#     data: {"name":name, "date":date}
#     doc_ref = db.collection("tournament").add(data)
# addTournament("Nuevo torneo", "01-10-2024")