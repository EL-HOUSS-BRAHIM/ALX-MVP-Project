#!/usr/bin/python3
import jwt
import datetime

SECRET_KEY = "alx-297bross-brahim-secret-key-2973-foralltimeloki-oh-doo-god-thing-time-doctor-who-data-i-like-it"

def checkJWTExpiration(token):
    """
    Check if a JSON Web Token (JWT) is expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        expiration_time = payload.get('exp')
        if expiration_time is None:
            return False

        current_time = datetime.datetime.utcnow()
        expiration_datetime = datetime.datetime.fromtimestamp(expiration_time)

        if current_time >= expiration_datetime:
            return False
        else:
            return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False

def generateJWT(payload, expiration_time=datetime.timedelta(hours=1)):
    """
    Generate a JSON Web Token (JWT) with the provided payload.
    """
    payload['exp'] = datetime.datetime.utcnow() + expiration_time
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token
