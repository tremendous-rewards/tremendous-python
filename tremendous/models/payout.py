# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Payout(BaseModel):
    """
    Payout
    """ # noqa: E501
    id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Tremendous ID of the payout")
    status: Optional[StrictStr] = None
    product_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Tremendous ID of the paid out product")
    product_name: Optional[StrictStr] = Field(default=None, description="Name of the paid out Product")
    created_at: Optional[datetime] = Field(default=None, description="Date the payout was created")
    executed_at: Optional[datetime] = Field(default=None, description="Date the payout was executed")
    __properties: ClassVar[List[str]] = ["id", "status", "product_id", "product_name", "created_at", "executed_at"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[A-Z0-9]{4,20}", value):
            raise ValueError(r"must validate the regular expression /[A-Z0-9]{4,20}/")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UNEXECUTED', 'COMPLETED', 'FAILED', 'CANCELED', 'ORGANIZATION_REVIEW', 'ADMIN_HELD']):
            raise ValueError("must be one of enum values ('UNEXECUTED', 'COMPLETED', 'FAILED', 'CANCELED', 'ORGANIZATION_REVIEW', 'ADMIN_HELD')")
        return value

    @field_validator('product_id')
    def product_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[A-Z0-9]{4,20}", value):
            raise ValueError(r"must validate the regular expression /[A-Z0-9]{4,20}/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Payout from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "product_id",
            "product_name",
            "created_at",
            "executed_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Payout from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "product_id": obj.get("product_id"),
            "product_name": obj.get("product_name"),
            "created_at": obj.get("created_at"),
            "executed_at": obj.get("executed_at")
        })
        return _obj

