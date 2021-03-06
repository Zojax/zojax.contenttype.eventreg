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
""" registration implementation

$Id$
"""
from zope import interface, component
from zope.proxy import removeAllProxies
from zope.cachedescriptors.property import Lazy
from zope.lifecycleevent.interfaces import IObjectModifiedEvent
from zojax.richtext.field import RichTextProperty
from zojax.content.type.item import PersistentItem
from zojax.content.type.searchable import ContentSearchableText

from interfaces import IEventRegRegistration


class EventRegRegistration(PersistentItem):

    interface.implements(IEventRegRegistration)
