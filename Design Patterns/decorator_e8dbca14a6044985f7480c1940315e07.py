class Text:

    def __init__(self,msg):
        self.msg=msg
    
    def show(self):
        return self.msg

class Bold(Text):

    def __init__(self,msg):
        self.boldmsg=msg
    
    def show(self):
        return "<b>{}</b>".format(self.boldmsg.show())

class Underline(Text):

    def __init__(self,msg):
        self.linemsg=msg
    
    def show(self):
        return "<u>{}</u>".format(self.linemsg.show())

class Italic(Text):

    def __init__(self,msg):
        self.itmsg=msg
    
    def show(self):
        return "<i>{}</i>".format(self.itmsg.show())

t=Text('Harish')
i=Underline(Italic(Bold(t)))
print(i.show())






