from models import Role, User


class RoleRepository:
    """
    A repository of Role objects.
    """

    def __init__(self, session):
        self.__session = session

    def add(self, role: Role):
        """
        Add a role object to the session.

        :param role: A Role object
        :return: None
        """
        self.__session.add(role)

    def get(self, id: int) -> Role:
        """
        Get a role object with the given id.

        :param id: int
        :return: A Role object
        """
        return self.__session.query(Role).get(id)


class UserRepository:
    """
    A repository for User objects.
    """

    def __init__(self, session):
        self.__session = session

    def add(self, user: User):
        """
        Add a user object to the session.

        :param user: A User object
        :return: None
        """
        self.__session.add(user)

    def get(self, id: int) -> User:
        """
        Get a user object with the given id.

        :param id: int
        :return: A User object
        """
        return self.__session.query(User).get(id)
