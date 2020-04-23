from pyink_types import Token, StringVar, Choice, KnotDefinition, StitchDef
from typing import Type, Optional, List


class Scanner:
    def __init__(self, file_name: str):
        with open(file_name, "r") as file:
            self.text: str = file.read()
        self.tokens: List[Token] = []

    def emit_token(self, token_type: Type, *args, **kwargs) -> None:
        self.tokens.append(token_type(*args, **kwargs))

    def scan_tokens(self):
        line_count: int = 0
        token_type: Type = StringVar
        could_be_comment: bool = False
        is_inline_comment: bool = False
        is_block_comment: bool = False
        block_comment_out: int = 0  # When 2 exit block comment.
        token: str = ""
        for char_ in self.text:
            if char_ == "=" and token_type == Token:
                token_type = StitchDef
            elif char_ == "=" and token_type == StitchDef:
                token_type = KnotDefinition
            elif char_ == "=":
                pass  # Ignore = otherwise.
            elif char_ == "/" and is_block_comment and block_comment_out == 1:
                is_block_comment = False
            elif char_ == "/" and could_be_comment:
                is_inline_comment = True
            elif char_ == "*" and is_block_comment:
                block_comment_out = 1
            elif char_ == "*" and could_be_comment:
                is_block_comment = True
            elif is_block_comment or is_inline_comment:
                block_comment_out = 0
            elif char_ == "*":
                token_type = Choice
            elif char_ == "\n":
                self.emit_token(token_type, line_count, token)
                token_type = StringVar
                token = ""
                line_count += 1
            else:
                token += char_
