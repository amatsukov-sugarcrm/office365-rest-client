# -*- coding: utf-8 -*-
from .services import OutlookService
from .services import CalendarService
from .services import AttachmentService


class Office365Client(object):
    api_version = 'v1.0'

    def __init__(self, http):
        self.http = http
        self.outlook = OutlookService(self)
        self.calendar = CalendarService(self)
        self.attachment = AttachmentService(self)
