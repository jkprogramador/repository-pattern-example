from sqlalchemy import (Table, MetaData, Column, Integer, String, DateTime,
                        ForeignKey)
from sqlalchemy.orm import mapper, relationship
import datetime as dt

from models import Role, User

metadata = MetaData()

roles = Table(
    "roles", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50), nullable=False, unique=True),
    Column("created_at", DateTime, nullable=False,
           server_default=dt.datetime.utcnow().strftime("%Y-%m-%d %R:%S")),
    Column("updated_at", DateTime, nullable=True)
)

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(50), nullable=False, unique=True, index=True),
    Column("email", String(200), nullable=False, unique=True, index=True),
    Column("password", String(200), nullable=False),
    Column("role_id", Integer, ForeignKey("roles.id"), nullable=False),
    Column("created_at", DateTime, nullable=False,
           server_default=dt.datetime.utcnow().strftime("%Y-%m-%d %R:%S")),
    Column("updated_at", DateTime, nullable=True)
)


def start_mappers():
    roles_mapper = mapper(Role, roles, properties={
        "users": relationship(
            User,
            back_populates="role"
        )
    })
    mapper(User, users, properties={
        "role": relationship(
            roles_mapper,
            back_populates="users"
        )
    })
