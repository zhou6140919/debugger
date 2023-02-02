"""My custom debugger"""
from icecream import IceCreamDebugger
import typer
import q
import pysnooper


class Debugger(IceCreamDebugger):

    def __init__(self):
        super().__init__()
        self.run = typer.run
        self.d = q.d
        self.snoop = pysnooper.snoop


ic = Debugger()
