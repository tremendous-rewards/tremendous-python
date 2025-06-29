# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and its members within Tremendous, please see the Tremendous Organizational API.

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
from tremendous.models.connected_organization_member_member import ConnectedOrganizationMemberMember
from typing import Optional, Set
from typing_extensions import Self

class ConnectedOrganizationMember(BaseModel):
    """
    ConnectedOrganizationMember
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)] = Field(description="Tremendous' identifier for the connected organization member.")
    external_name: Optional[StrictStr] = Field(default=None, description="The name associated with the user in your systems.")
    external_email: Optional[StrictStr] = Field(default=None, description="The email associated with the user in your systems.")
    created_at: datetime = Field(description="Timestamp of when the connected organization member was created.")
    connected_organization_id: Annotated[str, Field(strict=True)] = Field(description="Tremendous' identifier for the connected organization.")
    member: Optional[ConnectedOrganizationMemberMember] = None
    __properties: ClassVar[List[str]] = ["id", "external_name", "external_email", "created_at", "connected_organization_id", "member"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"[A-Z0-9]{4,20}", value):
            raise ValueError(r"must validate the regular expression /[A-Z0-9]{4,20}/")
        return value

    @field_validator('connected_organization_id')
    def connected_organization_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of ConnectedOrganizationMember from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "connected_organization_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of member
        if self.member:
            _dict['member'] = self.member.to_dict()
        # set to None if external_name (nullable) is None
        # and model_fields_set contains the field
        if self.external_name is None and "external_name" in self.model_fields_set:
            _dict['external_name'] = None

        # set to None if external_email (nullable) is None
        # and model_fields_set contains the field
        if self.external_email is None and "external_email" in self.model_fields_set:
            _dict['external_email'] = None

        # set to None if member (nullable) is None
        # and model_fields_set contains the field
        if self.member is None and "member" in self.model_fields_set:
            _dict['member'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectedOrganizationMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "external_name": obj.get("external_name"),
            "external_email": obj.get("external_email"),
            "created_at": obj.get("created_at"),
            "connected_organization_id": obj.get("connected_organization_id"),
            "member": ConnectedOrganizationMemberMember.from_dict(obj["member"]) if obj.get("member") is not None else None
        })
        return _obj


