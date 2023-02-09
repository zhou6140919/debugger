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
import atexit
import os
import time


class Debugger(IceCreamDebugger):

    def __init__(self):
        super().__init__()
        self.d = q.d
        self.snoop = pysnooper.snoop

    def init(self, sender=None, receiver=None, key=None):
        sys.excepthook = self.catch_exceptions
        self.file_name = os.path.abspath(sys.argv[0])
        self.sender = sender
        if receiver is None:
            self.receiver = sender
        else:
            self.receiver = receiver
        self.key = key
        self.exception: bool = False
        atexit.register(self.send_email)

    def send_email(self):
        if not (self.sender and self.receiver and self.key):
            return None
        """send email to notify user"""
        # TODO: Only QQ & Gmail is supported
        if 'gmail' in self.sender:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        elif 'qq' in self.sender:
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(self.sender, self.key)
        content = "Your job has failed. Here is the traceback info:\n"
        msg = MIMEMultipart()
        from datetime import datetime
        presesnt_time = str(datetime.now())
        code_part1 = """<pre style="font-weight: normal; font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; font-size: 14px; white-space: pre-wrap; background-color: #F4F5F6; color: #3D4649; border-radius: 4px; overflow-wrap: break-word; word-wrap: break-word; margin: 0 0 15px; padding: 15px">"""
        code_part2 = """</pre>"""
        def embed_html(x): return code_part1 + x + code_part2
        def change_html(x): return x.replace(
            "<code>", code_part1).replace("</code>", code_part2)
        if self.exception:
            html = "<h1>"+content+"</h1>"+change_html(self.traceback_info_text)
            msg['Subject'] = "Python Job Failed -> " + self.error_type
        else:
            msg['Subject'] = "Python Job Finished Succesfully!"
            html = """
            <h1>Congratulations!!!</h1>
            <p>Python Job finished without error</p>
            """ + embed_html(self.file_name)
        html += embed_html(presesnt_time.split('.')[0])
        msg.attach(MIMEText(html, 'html'))
        msg['From'] = self.sender
        server.sendmail(self.sender, self.receiver, msg.as_string())

    def catch_exceptions(self, t, val, tb):
        console_stderr = Console(stderr=True, record=True)

        rich_tb = Traceback.from_exception(
            t, val, tb, show_locals=True
        )
        # rich_tb.trace.stacks[0].frames = rich_tb.trace.stacks[0].frames[1:]
        console_stderr.print(rich_tb)
        self.traceback_info_text = console_stderr.export_html()
        if str(val):
            self.error_type = t.__name__ + ': ' + str(val)
        else:
            self.error_type = t.__name__
        self.exception = True

        return

    @staticmethod
    def countdown(time_elaspe):
        while time_elaspe:
            mins, secs = divmod(time_elaspe, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            time_elaspe -= 1


ic = Debugger()
