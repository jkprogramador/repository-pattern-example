from models import User, Role
from repositories import UserRepository


class TestUserRepository:
    """
    Test the User Repository for creating and retrieving User objects.
    """

    def test_create_user(self, session):
        """
        Assert that creating a User object is successful.

        GIVEN a User object with an associated Role\n
        WHEN adding that object to the repository\n
        THEN a user record with a role should be created in the database

        :param session: A fixture
        :return: None
        """
        user = User(username="joe", email="joe@gmail.com", password="123",
                    role=Role(name="visitor"))
        user_repo = UserRepository(session)
        user_repo.add(user)
        session.commit()

        rows = list(
            session.execute("SELECT username, email, role_id FROM users"))
        assert rows == [("joe", "joe@gmail.com", 1)]

    def test_read_user(self, session):
        """
        Assert that retrieving a user is successful.

        GIVEN a user record and an associated role in the database\n
        WHEN getting that user from the repository\n
        THEN the user record and its associated role should be retrieved from the database

        :param session: A fixture
        :return: None
        """
        session.execute("INSERT INTO roles (name) VALUES ('admin')")
        [[role_id]] = list(session.execute("SELECT id FROM roles WHERE name='admin'"))
        session.execute(
            "INSERT INTO users (username, email, password, role_id) \
             VALUES (:username, :email, :password, :role_id)",
            dict(username="joe", email="joe@gmail.com", password="123",
                 role_id=role_id))
        [[user_id]] = list(
            session.execute("SELECT id FROM users WHERE username='joe'"))
        user_repo = UserRepository(session)
        user = user_repo.get(user_id)
        assert user.id == 1
        assert user.username == "joe"
        assert user.email == "joe@gmail.com"
        assert user.role.name == "admin"
        assert user.role.id == 1
