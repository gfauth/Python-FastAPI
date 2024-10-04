from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_regitry = registry()


@table_regitry.mapped_as_dataclass
class User:
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    createdAt: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updatedAt: Mapped[datetime] = mapped_column(init=False, server_default=func.now(), onupdate=func.now())
