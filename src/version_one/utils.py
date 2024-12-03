from rest_framework.response import Response

def Res(status, message, error=None, content=None):
    res = {
        'status': status,
        'message': message,
    }
    if error is not None:
        res['error'] = error
    if content is not None:
        res['content'] = content
    return Response(res, status=status)