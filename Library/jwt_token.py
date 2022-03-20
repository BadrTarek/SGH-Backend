
import datetime
import jwt  # https://pyjwt.readthedocs.io/en/latest/usage.html


def generate_JWT_token(object) -> str:
    payload = {
        'id': object.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow(),
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256',
                       headers={'AUTH_HEADER_TYPES': ('Bearer',)})
    return token


def check_token(token):
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        return False

    return True
