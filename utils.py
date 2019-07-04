# -*- coding: utf-8 -*-
import re
import datetime
import urllib
import urlparse


RE_EMAIL = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))


def regex_extractor(regex, text, group):
    data = None
    if regex and text:
        data_search = re.search(regex, text, re.IGNORECASE | re.DOTALL | re.MULTILINE)
        if data_search:
            data = data_search.group(group).strip()
    return data


def convert_date_string(date_string, old_format, new_format):
    converted = None
    if date_string and old_format and new_format:
        date = datetime.datetime.strptime(date_string, old_format)
        converted = date.strftime(new_format)
    return converted


def extract_min_int_from_string(x):
    min_value = None
    if x:
        numbers = re.findall("\d+", x)
        if numbers:
            min_value = min(numbers)
    return min_value


def extract_emails(x):
    """Returns an iterator of matched emails found in string s."""
    # Removing lines that start with '//' because the regular expression
    # mistakenly matches patterns like 'http://foo@bar.com' as '//foo@bar.com'.
    emailGen = (email[0] for email in re.findall(RE_EMAIL, x) if not email[0].startswith("//"))
    return list(set(emailGen))


def add_params_to_url(url, **kwargs):
    """
    Add all kwargs as params to url
    """
    # Split url on parts
    url_parts = list(urlparse.urlparse(url))
    # Convert query parameters to dict
    query = dict(urlparse.parse_qsl(url_parts[4]))
    # Append to kwargs to this dict
    query.update(kwargs)

    # Make new url with parameters
    url_parts[4] = urllib.urlencode(query)
    return urlparse.urlunparse(url_parts)


