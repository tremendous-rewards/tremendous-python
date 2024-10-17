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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateOrganizationCopySettings(BaseModel):
    """
    A list of the settings that you wish to copy over to the new organization.
    """ # noqa: E501
    campaigns: Optional[StrictBool] = Field(default=False, description="Copy over the campaigns from the current organization to the new organization. Defaults to `false`.")
    custom_fields: Optional[StrictBool] = Field(default=False, description="Copy over the custom fields from the current organization to the new organization. Defaults to `false`.")
    order_approvals: Optional[StrictBool] = Field(default=False, description="Copy over the order approvals settings from the current organization to the new organization. Defaults to `false`.")
    payment_methods: Optional[StrictBool] = Field(default=False, description="Copy over the payment methods from the current organization to the new organization. Defaults to `false`.")
    security_settings: Optional[StrictBool] = Field(default=True, description="Copy over the security settings from the current organization to the new organization. Defaults to `true`.")
    users: Optional[StrictBool] = Field(default=False, description="Copy over the users and custom roles from the current organization to the new organization. Defaults to `false`.")
    custom_roles: Optional[StrictBool] = Field(default=False, description="Copy over the custom roles from the current organization to the new organization. Custom roles are always copied if `users` is `true`. Defaults to `false`.")
    fraud_prevention: Optional[StrictBool] = Field(default=False, description="Copy over the fraud prevention settings and rules from the current organization to the new organization. Defaults to `false`.")
    __properties: ClassVar[List[str]] = ["campaigns", "custom_fields", "order_approvals", "payment_methods", "security_settings", "users", "custom_roles", "fraud_prevention"]

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
        """Create an instance of CreateOrganizationCopySettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrganizationCopySettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "campaigns": obj.get("campaigns") if obj.get("campaigns") is not None else False,
            "custom_fields": obj.get("custom_fields") if obj.get("custom_fields") is not None else False,
            "order_approvals": obj.get("order_approvals") if obj.get("order_approvals") is not None else False,
            "payment_methods": obj.get("payment_methods") if obj.get("payment_methods") is not None else False,
            "security_settings": obj.get("security_settings") if obj.get("security_settings") is not None else True,
            "users": obj.get("users") if obj.get("users") is not None else False,
            "custom_roles": obj.get("custom_roles") if obj.get("custom_roles") is not None else False,
            "fraud_prevention": obj.get("fraud_prevention") if obj.get("fraud_prevention") is not None else False
        })
        return _obj


