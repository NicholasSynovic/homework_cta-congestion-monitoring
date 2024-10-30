from abc import ABCMeta
from typing import Any


class Schema(ABCMeta):
    pass


class LStops(Schema):
    def __init__(self) -> None:
        self.schema: dict[str, Any] = {
            "$schema": "http://json-schema.org/draft-06/schema#",
            "$ref": "#/definitions/LStops",
            "definitions": {
                "LStops": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "stop_id": {"type": "string", "format": "integer"},
                        "direction_id": {"type": "string"},
                        "stop_name": {"type": "string"},
                        "station_name": {"type": "string"},
                        "station_descriptive_name": {"type": "string"},
                        "map_id": {"type": "string", "format": "integer"},
                        "ada": {"type": "boolean"},
                        "red": {"type": "boolean"},
                        "blue": {"type": "boolean"},
                        "g": {"type": "boolean"},
                        "brn": {"type": "boolean"},
                        "p": {"type": "boolean"},
                        "pexp": {"type": "boolean"},
                        "y": {"type": "boolean"},
                        "pnk": {"type": "boolean"},
                        "o": {"type": "boolean"},
                        "location": {"$ref": "#/definitions/Location"},
                        ":@computed_region_awaf_s7ux": {
                            "type": "string",
                            "format": "integer",
                        },
                        ":@computed_region_6mkv_f3dw": {
                            "type": "string",
                            "format": "integer",
                        },
                        ":@computed_region_vrxf_vc4k": {
                            "type": "string",
                            "format": "integer",
                        },
                        ":@computed_region_bdys_3d7i": {
                            "type": "string",
                            "format": "integer",
                        },
                        ":@computed_region_43wa_7qmu": {
                            "type": "string",
                            "format": "integer",
                        },
                    },
                    "required": [
                        ":@computed_region_43wa_7qmu",
                        ":@computed_region_6mkv_f3dw",
                        ":@computed_region_awaf_s7ux",
                        ":@computed_region_bdys_3d7i",
                        ":@computed_region_vrxf_vc4k",
                        "ada",
                        "blue",
                        "brn",
                        "direction_id",
                        "g",
                        "location",
                        "map_id",
                        "o",
                        "p",
                        "pexp",
                        "pnk",
                        "red",
                        "station_descriptive_name",
                        "station_name",
                        "stop_id",
                        "stop_name",
                        "y",
                    ],
                    "title": "LStops",
                },
                "Location": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "latitude": {"type": "string"},
                        "longitude": {"type": "string"},
                        "human_address": {"type": "string"},
                    },
                    "required": ["human_address", "latitude", "longitude"],
                    "title": "Location",
                },
            },
        }
