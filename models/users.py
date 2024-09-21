import helpers.utils

# Model Base
from . import Base

# Sqlalchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=helpers.utils.GeneratorUUID, index=True)