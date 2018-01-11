import json

statusCode = {
    200: 'Success.',
    1000: 'Username already exists.',
    1001: 'Invalid sername pattern.',
    1002: 'Password too long.',
}


def getStatusJson(num):
    return {'status': num, 'message': statusCode[num]}
