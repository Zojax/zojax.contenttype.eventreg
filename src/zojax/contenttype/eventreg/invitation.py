from zope.interface import implements
from zope import component

from interfaces import IInvitation

class Invitation(object):

    implements(IInvitation)

    firstName = u''
    lastName = u''
    email = u''
