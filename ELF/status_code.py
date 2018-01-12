import json

statusCode = {
    200: 'Success.',
    1000: 'Username already exists.',
    1001: 'Invalid sername pattern.',
    1002: 'Password too long.',
    1003: 'Invalid username or password.',
    1004: 'Permission denied.',
}


def getStatusJson(num):
    return {'status': num, 'message': statusCode[num]}
