"""
The functions in this file are designed to query thegamesdb.net API
and return a list of the results
"""

import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs


def get_games_list(name, platform=None, genre=None):
    """
    getGamesList(name [, platform, genre])

    The GetGamesList API search returns a listing of games matched up with
    loose search terms.

    http://wiki.thegamesdb.net/index.php?title=GetGamesList
    """

    url = "http://thegamesdb.net/api/GetGamesList.php"

    params = {"name": name}

    if platform:
        params["platform"] = platform

    if genre:
        # This doesn't seem to be functional as of 2/10/2015
        params["genre"] = genre

    content, encoding = _fetch_url(url, params)

    bsc = bs(content)

    games = []
    for game in bsc.find_all('game'):
        try:
            date = game.releasedate.string
        except:
            date = None
        d = {'id': game.id.string,
             'title': game.gametitle.string,
             'release_date': date,
             'platform': game.platform.string,
             }
        games.append(d)

    # This could writes results into a file get_games_list_name_YYYYMMDD.txt
    # _write_results("get_games_list", content, name)

    # Currently returns results as XML string.
    # This can be altered to any other format

    return games


def get_platform_names():
    """
    Returns a list of all the platform names.

    http://wiki.thegamesdb.net/index.php?title=GetPlatformsList
    """
    url = 'http://thegamesdb.net/api/GetPlatformsList.php'
    content, encoding = _fetch_url(url, None)
    # grab names out of the xml string
    bsc = bs(content)
    names_xml = bsc.find_all('name')
    names = []
    for name in names_xml:
        names.append(name.text)
    return names


def _fetch_url(url, params):
    resp = requests.get(url, params=params)
    if resp.ok:
        return resp.content, resp.encoding
    else:
        return resp.raise_for_status()


def _write_results(function, content, keyword):
    timestamp = datetime.now()
    filename = '%s_%s_%s.txt' % (function, keyword, timestamp.strftime('%Y%m%d'))
    with open(filename, 'w') as outfile:
        outfile.write(content)
