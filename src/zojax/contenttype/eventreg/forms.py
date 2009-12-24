##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zojax.content.browser.form import Fields, EditForm, AddForm

from interfaces import IEventReg, IEventRegGroup, IEventRegRegistration, IAttendee
from listwidget import ListFieldWidget
import attendee
from z3c.form.object import registerFactoryAdapter

class EventRegAddForm(AddForm):

    fields = Fields(IEventReg)

class EventRegGroupAddForm(AddForm):

    fields = Fields(IEventRegGroup)

class EventRegRegistrationAddForm(AddForm):

    fields = Fields(IEventRegRegistration).omit('title',  'surveys', 'invitations')

registerFactoryAdapter(IAttendee, attendee.Attendee)


class EventRegEditForm(EditForm):

    fields = Fields(IEventReg)

class EventRegGroupEditForm(EditForm):

    fields = Fields(IEventRegGroup)

class EventRegRegistrationEditForm(EditForm):

    fields = Fields(IEventRegRegistration).omit('title', 'surveys', 'invitations')
