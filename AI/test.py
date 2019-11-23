import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

DB_link='https://guardians-of-energy.firebaseio.com/'
DB_cred='./GOE.json'

firebase_admin.initialize_app(credentials.Certificate(DB_cred), {
    'databaseURL' : DB_link
})

ref = db.reference()
print(ref.get())