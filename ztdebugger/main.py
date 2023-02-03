"""My custom debugger"""
import sys
from icecream import IceCreamDebugger
import q
import pysnooper
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rich.console import Console
from rich.traceback import Traceback


class Debugger(IceCreamDebugger):

    def __init__(self):
        super().__init__()
        self.d = q.d
        self.snoop = pysnooper.snoop

    def init(self, sender=None, receiver=None, key=None):
        sys.excepthook = self.catch_exceptions
        self.sender = sender
        if receiver is None:
            self.receiver = sender
        else:
            self.receiver = receiver
        self.key = key

    def send_email(self, error_type, traceback_info, sender, receiver, key):
        """send email to notify user"""
        # TODO: Only QQ is supported
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, key)
        content = f"Your job has failed. Here is the traceback info:\n{traceback_info}"
        msg = MIMEMultipart()
        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        msg['Subject'] = "Python Job Failed -> " + error_type
        msg['From'] = sender
        server.sendmail(sender, receiver, msg.as_string())

    def catch_exceptions(self, t, val, tb):
        console_stderr = Console(stderr=True, record=True)

        rich_tb = Traceback.from_exception(
            t, val, tb, show_locals=True
        )
        rich_tb.trace.stacks[0].frames = rich_tb.trace.stacks[0].frames[1:]
        console_stderr.print(rich_tb)
        traceback_info = console_stderr.export_text()
        error_type = t.__name__ + ': ' + str(val)
        if self.sender and self.receiver and self.key:
            self.send_email(error_type, traceback_info, self.sender,
                            self.receiver, self.key)

        return


ic = Debugger()
