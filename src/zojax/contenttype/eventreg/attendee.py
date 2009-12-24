from zope.interface import implements
from zope import component

from interfaces import IAttendee

class Attendee(object):

    implements(IAttendee)

    title = u''
    first_name = u''
    last_name = u''
    company = u''
    address_1 = u''
    address_2 = u''
    city = u''
    state = u''
    country = u''
    zip_postal = u''
    phone = u''
    cell_phone = u''
    email = u''
    is_member = False
