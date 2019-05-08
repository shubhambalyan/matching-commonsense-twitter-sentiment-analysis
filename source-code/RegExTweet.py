# -*- coding: utf-8 -*-
"""
"""
import re
import urllib

AT_SIGNS = ur'[@\uff20]'
UTF_CHARS = ur'a-z0-9_\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff'
SPACES = ur'[\u0020\u00A0\u1680\u180E\u2002-\u202F\u205F\u2060\u3000]'

# Lists
LIST_PRE_CHARS = ur'([^a-z0-9_]|^)'
LIST_END_CHARS = ur'([a-z0-9_]{1,20})(/[a-z][a-z0-9\x80-\xFF-]{0,79})?'
LIST_REGEX = re.compile(LIST_PRE_CHARS + '(' + AT_SIGNS + '+)' + LIST_END_CHARS,
                        re.IGNORECASE)

# Users
USERNAME_REGEX = re.compile(ur'\B' + AT_SIGNS + LIST_END_CHARS, re.IGNORECASE)
REPLY_REGEX = re.compile(ur'^(?:' + SPACES + ur')*' + AT_SIGNS \
              + ur'([a-z0-9_]{1,20}).*', re.IGNORECASE)

# Hashtags
HASHTAG_EXP = ur'(^|[^0-9A-Z&/]+)(#|\uff03)([0-9A-Z_]*[A-Z_]+[%s]*)' % UTF_CHARS
HASHTAG_REGEX = re.compile(HASHTAG_EXP, re.IGNORECASE)


# URLs
PRE_CHARS = ur'(?:[^/"\':!=]|^|\:)'
DOMAIN_CHARS = ur'([\.-]|[^\s_\!\.\/])+\.[a-z]{2,}(?::[0-9]+)?'
PATH_CHARS = ur'(?:[\.,]?[%s!\*\'\(\);:=\+\$/%s#\[\]\-_,~@])' % (UTF_CHARS, '%')
QUERY_CHARS = ur'[a-z0-9!\*\'\(\);:&=\+\$/%#\[\]\-_\.,~]'

# Valid end-of-path chracters (so /foo. does not gobble the period).
# 1. Allow ) for Wikipedia URLs.
# 2. Allow =&# for empty URL parameters and other URL-join artifacts
PATH_ENDING_CHARS = r'[%s\)=#/]' % UTF_CHARS
QUERY_ENDING_CHARS = '[a-z0-9_&=#]'

URL_REGEX = re.compile('((%s)((https?://|www\\.)(%s)(\/%s*%s?)?(\?%s*%s)?))'
                       % (PRE_CHARS, DOMAIN_CHARS, PATH_CHARS,
                          PATH_ENDING_CHARS, QUERY_CHARS, QUERY_ENDING_CHARS),
                          re.IGNORECASE)
#text = '#Twitter are you freaking kidding me #wth... http://t.co/zKn2bu5R'
#text = 'Which planet is he living on... #Microsoft #CEO #Fail #palmface http://t.co/3zcq60SF'
#text = "I've seen a couple of iPhone 4S's already, but still no Windows Phone 7's ... ever! #Microsoft not so hot."
text = "[WebProNews Finance] #Yahoo Revenue Drop Attributed to #Microsoft Deal http://t.co/ItdkLRry"
text=  re.sub(USERNAME_REGEX,'',text)
text=  re.sub(HASHTAG_REGEX,'',text)
text=  re.sub(REPLY_REGEX,'',text)
text=  re.sub(URL_REGEX,'',text)
text = text.replace('.','')
print text