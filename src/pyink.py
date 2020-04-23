from pyink_types import Token, stringVar, Choice, KnotDefinition, StitchDef
from typing import Type, Optional, Dict


class Scanner:
    def __init__(self, file_name: str):
        with open(file_name, "r") as file:
            self.text: str = file.read()

    @staticmethod
    def emit_token(token_type: Type, *args, **kwargs) -> Token:
        return token_type(*args, **kwargs)

    def scan_tokens(self):
        line_count: int = 0
        token_type: Type = Token
        could_be_comment: bool = False
        is_inline_comment: bool = False
        is_block_comment: bool = False
        token = None
        for char_ in self.text:
            if char_ == "=" and token_type == Token:
                token_type = StitchDef
            elif char_ == "=" and token_type == StitchDef:
                token_type = KnotDefinition
            elif char_ == "=":
                pass  # Ignore = otherwise.
            elif char_ == "/" and could_be_comment:
                is_inline_comment = True
            elif char_ == "*" and could