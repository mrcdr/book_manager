import os
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

BM_ADMIN_NAME = os.environ["BM_ADMIN_NAME"]
BM_ADMIN_PASSWORD = generate_password_hash(os.environ["BM_ADMIN_PASSWORD"])
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username == BM_ADMIN_NAME and  check_password_hash(BM_ADMIN_PASSWORD, password):
        return username
