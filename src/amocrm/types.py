from dataclasses import asdict
from dataclasses import dataclass

from _decimal import Decimal


@dataclass(frozen=True)
class AmoCRMCatalog:
    id: int
    name: str
    type: str

    @classmethod
    def from_json(cls, data: dict) -> "AmoCRMCatalog":
        return cls(id=data["id"], name=data["name"], type=data["type"])


@dataclass(frozen=True)
class AmoCRMCatalogFieldValue:
    value: str | int | Decimal
    id: int | None = None

    def to_json(self) -> dict:
        return {key: value for key, value in asdict(self).items() if value is not None}

    @classmethod
    def from_json(cls, data: dict) -> "AmoCRMCatalogFieldValue":
        return cls(id=data["id"], value=data["value"])


@dataclass(frozen=True)
class AmoCRMCatalogField:
    id: int
    name: str
    type: str
    code: str
    nested: list[AmoCRMCatalogFieldValue] | None = None

    @classmethod
    def from_json(cls, data: dict) -> "AmoCRMCatalogField":
        nested = data.get("nested")
        if nested is not None:
            nested = [AmoCRMCatalogFieldValue.from_json(nested_data) for nested_data in nested]
        return cls(
            id=data["id"],
            name=data["name"],
            type=data["type"],
            code=data["code"],
            nested=nested,
        )


@dataclass(frozen=True)
class AmoCRMCatalogElementFieldValue:
    value: str | int | Decimal

    def to_json(self) -> dict:
        return {"value": str(self.value)}  # it stores as string in amocrm

    @classmethod
    def from_json(cls, data: dict) -> "AmoCRMCatalogElementFieldValue":
        return cls(value=data["value"])


@dataclass(frozen=True)
class AmoCRMCatalogElementField:
    """
    https://www.amocrm.ru/developers/content/crm_platform/custom-fields
    """

    field_id: int
    values: list[AmoCRMCatalogElementFieldValue]

    def to_json(self) -> dict:
        return {"field_id": self.field_id, "values": [value.to_json() for value in self.values]}

    @classmethod
    def from_json(cls, data: dict) -> "AmoCRMCatalogElementField":
        return cls(field_id=data["field_id"], values=[AmoCRMCatalogElementFieldValue.from_json(nested_data) for nested_data in data["values"]])


@dataclass(frozen=True)
class AmoCRMCatalogElement:
    name: str
    custom_fields_values: list[AmoCRMCatalogElementField]
    id: int | None = None

    def to_json(self) -> dict:
        if self.id is None:
            return {
                "name": self.name,
                "custom_fields_values": [field_value.to_json() for field_value in self.custom_fields_values],
            }
        else:
            return {
                "id": self.id,
                "name": self.name,
                "custom_fields_values": [field_value.to_json() for field_value in self.custom_fields_values],
            }

    @classmethod
    def from_json(cls, data: dict) -> "AmoCRMCatalogElement":
        return cls(
            id=data["id"],
            name=data["name"],
            custom_fields_values=[AmoCRMCatalogElementField.from_json(field_value) for field_value in data["custom_fields_values"]],
        )


@dataclass(frozen=True)
class AmoCRMPipelineStatus:
    id: int
    name: str

    @classmethod
    def from_json(cls, data: dict) -> "AmoCRMPipelineStatus":
        return cls(id=data["id"], name=data["name"])


@dataclass(frozen=True)
class AmoCRMPipeline:
    id: int
    name: str
    statuses: list[AmoCRMPipelineStatus]

    @classmethod
    def from_json(cls, data: dict) -> "AmoCRMPipeline":
        return cls(id=data["id"], name=data["name"], statuses=[AmoCRMPipelineStatus.from_json(status) for status in data["_embedded"]["statuses"]])
