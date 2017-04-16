from pyramid.security import Allow, Everyone, Authenticated
class BlogRecordFactory:
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, Authenticated, 'create'),
               (Allow, Authenticated, 'edit'),]


    def __init__(self, request):
        pass
