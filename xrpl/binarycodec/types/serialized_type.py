"""The base class for all binary codec field types."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional, Type, Union


class SerializedType(ABC):
    """The base class for all binary codec field types."""

    def __init__(self: SerializedType, buffer: bytes = bytes()) -> None:
        """Construct a new SerializedType."""
        self.buffer = buffer

    @classmethod
    @abstractmethod
    def from_parser(
        cls: Type[SerializedType],
        parser: Any,
        length_hint: Optional[int] = None
        # TODO: resolve Any (can't be `BinaryParser` because of circular imports)
    ) -> SerializedType:
        """
        Constructs a new SerializedType from a BinaryParser.

        Args:
            parser: The parser to construct a SerializedType from.
            length_hint: The number of bytes to consume from the parser.

        Raises:
            NotImplementedError: Always.
        """
        raise NotImplementedError("SerializedType.from_parser not implemented.")

    @classmethod
    @abstractmethod
    def from_value(cls: Type[SerializedType], value: Any) -> SerializedType:
        """
        Construct a new SerializedType from a literal value.

        Args:
            value: The value to construct the SerializedType from.

        Raises:
            NotImplementedError: Always.
        """
        raise NotImplementedError("SerializedType.from_value not implemented.")

    def to_byte_sink(self: SerializedType, bytesink: bytearray) -> None:
        """
        Write the bytes representation of a SerializedType to a bytearray.

        Args:
            bytesink: The bytearray to write self.buffer to.

        Returns: None
        """
        bytesink.extend(self.buffer)

    def to_bytes(self: SerializedType) -> bytes:
        """
        Get the bytes representation of a SerializedType.

        Returns:
            The bytes representation of the SerializedType.
        """
        return self.buffer

    def to_json(self: SerializedType) -> Union[str, int]:
        """
        Returns the JSON representation of a SerializedType.

        If not overridden, returns hex string representation of bytes.

        Returns:
            The JSON representation of the SerializedType.
        """
        return self.to_hex()

    def to_string(self: SerializedType) -> str:
        """
        Returns the hex string representation of self.buffer.

        Returns:
            The hex string representation of self.buffer.
        """
        return self.to_hex()

    def to_hex(self: SerializedType) -> str:
        """
        Get the hex representation of a SerializedType's bytes.

        Returns:
            The hex string representation of the SerializedType's bytes.
        """
        return self.buffer.hex().upper()

    def __len__(self: SerializedType) -> int:
        """Get the length of a SerializedType's bytes."""
        return len(self.buffer)
