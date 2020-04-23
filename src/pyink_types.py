from dataclasses import dataclass
from typing import List, final, Optional


@dataclass()
class Token:
    line_count: int


@dataclass()
class stringVar(Token):
    """
    Represents any string content in an .ink file.
    :param string: String representation of the content.
    """
    string: final(str)


@dataclass()
class Choice(Token):
    """
    Represents a choice.
    :param choiceStr: Text of the choice.
    :param contentBlock: Content tied to the choice.
    :param visited: If the choice is visited, defaults to False.
    """
    choiceStr: str
    contentBlock: Optional["ContentBlock"] = None
    visited: bool = False


@dataclass()
class StitchDef(Token):
    """
    Represents the definition of a stitch.
    """
    stitchName: str


@dataclass()
class KnotDefinition(Token):
    """
    Represents the definition of a knot.
    """
    knotName: str


@dataclass()
class ChoiceBlock:
    """
    A block of choices.
    :param choices: A list of choices the player can take.
    """
    choices: List[Choice]


@dataclass()
class ContentBlock:
    """
    A block of content.
    :param stringVar String representation of dialog.
    :param finazilizngChoiceBlock the choice block finalizing our content block.
    """
    stringVar: str
    finalizingChoiceBlock: ChoiceBlock


@dataclass()
class Stitch:
    """
    A stitch.
    :param content Content of the stitch.
    """
    definition: StitchDef
    content: List[ContentBlock]


@dataclass()
class Knot:
    """
    A knot.
    """
    stitches: List[Stitch]


@dataclass()
class Ink:
    author: final(str)
    title: final(str)
    knots: List[Knot]