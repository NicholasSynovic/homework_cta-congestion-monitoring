from typing import Any


class Schema:
    pass


class LStops(Schema):
    def __init__(self) -> None:
        self.schema: dict[str, Any] = {
            "$schema": "http://json-schema.org/draft-06/schema#",
            "type": "array",
            "items": {"$ref": "#/definitions/LStop"},
            "definitions": {
                "LStop": {
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
                    "title": "LStop",
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


class TrainArrivals(Schema):
    def __init__(self) -> None:
        self.schema: dict[str, Any] = {
            "$schema": "http://json-schema.org/draft-06/schema#",
            "$ref": "#/definitions/LStops",
            "definitions": {
                "LStops": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {"ctatt": {"$ref": "#/definitions/Ctatt"}},
                    "required": ["ctatt"],
                    "title": "LStops",
                },
                "Ctatt": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "tmst": {"type": "string", "format": "date-time"},
                        "errCd": {"type": "string", "format": "integer"},
                        "errNm": {"type": "null"},
                        "eta": {
                            "type": "array",
                            "items": {"$ref": "#/definitions/Eta"},
                        },
                    },
                    "required": ["errCd", "errNm", "eta", "tmst"],
                    "title": "Ctatt",
                },
                "Eta": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "staId": {"type": "string", "format": "integer"},
                        "stpId": {"type": "string", "format": "integer"},
                        "staNm": {"type": "string"},
                        "stpDe": {"type": "string"},
                        "rn": {"type": "string", "format": "integer"},
                        "rt": {"type": "string"},
                        "destSt": {"type": "string", "format": "integer"},
                        "destNm": {"type": "string"},
                        "trDr": {"type": "string", "format": "integer"},
                        "prdt": {"type": "string", "format": "date-time"},
                        "arrT": {"type": "string", "format": "date-time"},
                        "isApp": {"type": "string", "format": "integer"},
                        "isSch": {"type": "string", "format": "integer"},
                        "isDly": {"type": "string", "format": "integer"},
                        "isFlt": {"type": "string", "format": "integer"},
                        "flags": {"type": "null"},
                        "lat": {"type": ["string", "null"]},
                        "lon": {"type": ["string", "null"]},
                        "heading": {"type": ["string", "null"], "format": "integer"},
                    },
                    "required": [
                        "arrT",
                        "destNm",
                        "destSt",
                        "flags",
                        "heading",
                        "isApp",
                        "isDly",
                        "isFlt",
                        "isSch",
                        "lat",
                        "lon",
                        "prdt",
                        "rn",
                        "rt",
                        "staId",
                        "staNm",
                        "stpDe",
                        "stpId",
                        "trDr",
                    ],
                    "title": "Eta",
                },
            },
        }
