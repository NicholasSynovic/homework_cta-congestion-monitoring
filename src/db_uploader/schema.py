from json import load
from pathlib import Path

from jsonschema import ValidationError, validate


class Schema:
    def __init__(self, schemaPath: Path) -> None:
        self.schemaPath: Path = schemaPath
        self.schema: dict = load(fp=open(file=self.schemaPath))

    def compare(self, data: dict) -> bool:
        try:
            validate(instance=data, schema=self.schema)
        except ValidationError:
            return False
        else:
            return True
