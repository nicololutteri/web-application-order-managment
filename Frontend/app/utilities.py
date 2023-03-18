from enum import Enum
import jwt

def getUser(request):
    token = request.COOKIES.get('token', None)
    payload = jwt.decode(token, 'secret', 'HS256')

    return (payload['user_id'], getRole(payload['user_id']))

class Role(Enum):
    Customer = 1
    Agent = 2
    Manager = 3

def getRole(user: str) -> Role:
    if (user[0] == "M"):
        return Role.Manager
    elif (user[0] == "A"):
        return Role.Agent
    elif (user[0] == 'C'):
        return Role.Customer
    else:
        raise
