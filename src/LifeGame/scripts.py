"""
    LifeGame.scripts

This file contains any commands about LifeGame.
"""


""" imports """


from abc import ABC, abstractmethod


""" processes """

""" command skeleton """


class CommandSkeleton(ABC):
    """ Command class base """
    def __init__(self):
        """ Initialize command class """
        return

    @abstractmethod
    def __call__(self, *args, **kwargs):
        """ Call command process """
        return

    ...


""" command class initializer """


class Initializer:
    """ Command classes initializer """

    """ values """
    # instance
    args: tuple[any]
    kwargs: dict[str, any]

    def __init__(self, *args: any, **kwargs: any):
        """ Assign args """
        self.args = args
        self.kwargs = kwargs
        return

    def __call__(self, cls: CommandSkeleton):
        """ Initialize and replace class instance """
        return cls(*self.args, **self.kwargs)

    ...


""" LifeGame commands """


@Initializer()
class LifeGame(CommandSkeleton):
    """ LifeGame command """

    def __call__(self, *args, **kwargs):
        return

    ...

