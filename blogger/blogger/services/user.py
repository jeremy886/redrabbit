from ..models import User


class UserService:

    @classmethod
    def by_name(cls, name, request):
        return request.dbsession.query(User).filter(User.name == name).first()
