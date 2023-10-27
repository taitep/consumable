from dataclasses import dataclass, field


@dataclass
class Consumable:
    """
    Bool that resets to False when used.
    """

    value = field(default=False)
    reset = field(default=False)

    def __bool__(self):
        """
        Consume and return value.
        """

        value = self.value
        self.value = self.reset
        return value
