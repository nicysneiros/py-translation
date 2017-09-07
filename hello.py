import gettext


class ServiceMessages:
    def __init__(self, _, name):
        self.MY_NAME = _("My Name is {name}").format(name=name)


class Service:
    def __init__(self):
        pt = gettext.translation('hello', localedir='locale', languages=['pt'])
        self._ = pt.ugettext


class ServiceImpl(Service):

    def hello(self):
        service_message = ServiceMessages(self._, "Nicolle")
        s = self._("Hello World!")
        print s
        p = service_message.MY_NAME
        print p


# pt = gettext.translation('hello', localedir='locale', languages=['pt'])
# _ = pt.gettext

# s = _("Hello World!")

# print s
service = ServiceImpl()
service.hello()
