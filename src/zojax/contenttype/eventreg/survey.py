from zope.interface import implements
from zope import component

from interfaces import ISurvey

class Survey(object):

    implements(ISurvey)

    how = u''
    expect = u''
