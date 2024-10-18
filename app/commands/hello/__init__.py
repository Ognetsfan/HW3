import sys
from app.commands import Command


class HelloCommand(Command):
    def execute(self):
        print(f'Hi nice to meet you')