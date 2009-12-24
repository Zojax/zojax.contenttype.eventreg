##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
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
""" event interfaces

$Id$
"""
from zope import schema, interface
from z3c.schema.baseurl import BaseURL
from z3c.schema.email import RFC822MailAddress
from zojax.richtext.field import RichText
from zojax.contenttypes.interfaces import _
from zojax.calendar.interfaces import IEvent, IEventLocation
from vocabularies import vocabularies
from zojax.filefield.field import ImageField

class IEventReg(IEvent, IEventLocation):

    eventUrl = BaseURL(
        title = _(u'Event URL'),
        description = _(u'Web address with more info about the event.'),
        required = False)

    contactName = schema.TextLine(
        title = _(u'Contact Name'),
        required = False)

    contactEmail = RFC822MailAddress(
        title = _(u'Contact E-mail'),
        required = False)

    contactPhone = schema.TextLine(
        title = _(u'Contact Phone'),
        required = False)

    text = RichText(
        title = _(u'Body'),
        description = _(u'Event body text.'),
        required = False)

    cooked_text = interface.Attribute('Cooked text')

    linkToDirections = BaseURL(
        title=_(u"Link to Directions"),
        required=True
    )

    mapImage = ImageField(
        title=_(u'Map'),
        description=_(u'Image with map.'),
        required=False,
        )

    announcementComment = schema.TextLine(
        title=_(u'Announcement Comment'),
        description=_(u'Comment field will be displayed directly after To and From Time for example "10-11:30 (Lunch will be served)"'),
        required=False
    )

    emailComment = schema.Text(
        title=_(u'Email Comment'),
        description=_(u'Comment field will be displayed directly after To and From Time in the email that is sent to registrants'),
        required=True
    )

    managerEmails = schema.List(
        title=_(u'Manager Emails'),
        required=True,
        value_type=RFC822MailAddress(title=_(u"Manager Email"))
    )

class IEventRegType(interface.Interface):
    """ event reg content type """


class IEventRegGroup(interface.Interface):

    title = schema.TextLine(
        title = _(u'Title'),
        description = _(u'Event group title.'),
        required = True)

    description = schema.Text(
        title = _(u'Description'),
        description = _(u'A short summary of the event group.'),
        required = False)

    text = RichText(
        title = _(u'Body'),
        description = _(u'Event registrable group body text.'),
        required = False)

    cooked_text = interface.Attribute('Cooked text')


class IEventRegGroupType(interface.Interface):
    """ event reg group content type """

class IAttendee(interface.Interface):

    title = schema.Choice(
        title=_(u'Title'),
        vocabulary=vocabularies['TITLES'],
        required=False
    )

    firstName = schema.TextLine(
        title=_(u'First Name'),
        required=True
    )

    lastName = schema.TextLine(
        title=_(u'Last Name'),
        required=True
    )

    company = schema.TextLine(
        title=_(u'Company'),
        required=True
    )

    address1 = schema.TextLine(
        title=_(u'Address Line 1'),
        required=False
    )

    address2 = schema.TextLine(
        title=_(u'Address Line 2'),
        required=False
    )

    city = schema.TextLine(
        title=_(u'City'),
        required=False
    )

    state = schema.Choice(
        title=_(u'State'),
        vocabulary=vocabularies['STATES'],
        required=False
    )

    country = schema.Choice(
        title=_(u'Country'),
        vocabulary=vocabularies['COUNTRIES'],
        required=False
    )

    zipPostal = schema.TextLine(
        title=_(u'Zip (Postal Code)'),
        required=False
    )

    phone = schema.TextLine(
        title=_(u'Phone'),
        required=False
    )

    cellPhone = schema.TextLine(
        title=_(u'Cell Phone'),
        required=False
    )

    email = RFC822MailAddress(
        title=_(u'Email'),
        required=True
    )

    isMember = schema.Bool(
        title=_(u'Member'),
        default=False
    )

class ISurvey(interface.Interface):

    how = schema.Choice(
        title=_(u'How did you hear about this event'),
        vocabulary=vocabularies['SURVEY_HOW'],
        required=False
    )

    expect = schema.Text(
        title=_(u'Your expectations'),
        required=True
    )

class IInvitation(interface.Interface):

    firstName = schema.TextLine(
        title=_(u'First Name'),
        required=True
    )

    lastName = schema.TextLine(
        title=_(u'Last Name'),
        required=True
    )

    email = RFC822MailAddress(
        title=_(u'Email'),
        required=True
    )


class IEventRegRegistration(interface.Interface):

    title = schema.TextLine(
        title = _(u'Title'),
        description = _(u'Event registrable title.'),
        required = True)

    description = schema.Text(
        title = _(u'Comments or Questions'),
        description = _(u'A short summary of the event registrable registration.'),
        required = False)


    contactFirstName = schema.TextLine(
        title=_(u'Contact First Name'),
        required=True
    )

    contactLastName = schema.TextLine(
        title=_(u'Contact Last Name'),
        required=True
    )

    contactEmail = RFC822MailAddress(
        title=_(u'Contact Email'),
        required=True
    )

    contactPhone = schema.TextLine(
        title=_(u'Contact Day-Time Phone'),
        required=False
    )

    attendees =  schema.List(
        title = _(u'Attendees'),
        value_type = schema.Object(title = _(u'Attendee'),
                                   schema=IAttendee),
        required = True)

    surveys = schema.List(
        title = _('Surveys'),
        value_type = schema.Object(title = _(u'Survey'),
                                   schema=ISurvey),
        required = True)

    invitations = schema.List(
        title = _('Invitations'),
        value_type = schema.Object(title = _(u'Invitation'),
                                   schema=IInvitation),
        required = True)

class IEventRegRegistrationType(interface.Interface):
    """ event reg registration content type """
