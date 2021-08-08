from typing import Any, Generator
from abc import abstractmethod, ABC
from contextlib import asynccontextmanager

from data.queries.query import Query


class BaseConnection(ABC):
    """Connection to a DB"""

    @abstractmethod
    async def execute(self, query: Query, **values) -> None:
        pass

    @abstractmethod
    async def fetch(self, query: Query, **values) -> Any:
        pass


class BasePool(ABC):
    """
    Base Connection class for database operations.
    All methods decorated with abc.abstractmethod should be overriden
    in the derived class.
    """

    @abstractmethod
    # asynccontextmanager
    async def connection(self) -> BaseConnection:
        """Async generator method which yields a NEW Connection object"""
        raise NotImplementedError

    @abstractmethod
    async def release_connection(self) -> None:
        raise NotImplementedError
