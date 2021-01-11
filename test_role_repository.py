from models import Role
from repositories import RoleRepository


class TestRoleRepository:
    """
    Test the Role repository for creating and retrieving Role objects.
    """

    def test_create_role(self, session):
        """
        Assert that creating a role is successful.

        GIVEN an object Role\n
        WHEN adding that object to the repository\n
        THEN a role record should be created in the database

        :param session: A fixture
        :return: None
        """
        role = Role(name="admin")
        role_repo = RoleRepository(session)
        role_repo.add(role)
        session.commit()

        rows = list(session.execute("SELECT id, name FROM roles"))
        assert rows == [(1, "admin")]

    def test_read_role(self, session):
        """
        Assert that retrieving a role is successful.

        GIVEN a role record and a user record in the database\n
        WHEN getting that role from the repository\n
        THEN the role record along with the associated user should
        be retrieved from the database

        :param session: A fixture
        :return: None
        """
        session.execute(
            "INSERT INTO roles (name) VALUES (:name)",
            dict(name="visitor"))
        [[id]] = session.execute("SELECT id FROM roles WHERE name='visitor'")
        session.execute(
            f"INSERT INTO users (username, email, password, role_id) \
             VALUES ('joe', 'joe@gmail.com', '123', {id})")
        role_repo = RoleRepository(session)
        role = role_repo.get(id)
        assert role.name == "visitor"
        assert len(role.users) == 1
        assert role.users[0].username == "joe"
