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
            date = 'N/A'
        d = {'game_id': game.id.string,
             'title': game.gametitle.string,
             'release_date': date,
             'platform': game.platform.string,
             }
        games.append(d)

    # This could writes results into a file get_games_list_name_YYYYMMDD.txt
    # _write_results("get_games_list", content, name)

    # Currently returns results as a list of dictionaries for each game

    return games


def get_game_details(name, game_id=None, platform=None):
    """
    getGamesList(name [, platform, genre])

    The GetGamesList API search returns a listing of games matched up with
    loose search terms.

    http://wiki.thegamesdb.net/index.php?title=GetGamesList
    """

    url = "http://thegamesdb.net/api/GetGame.php"

    params = {"name": name}

    if platform:
        params["platform"] = platform

    if game_id:
        # This doesn't seem to be functional as of 2/10/2015
        params["id"] = game_id

    content, encoding = _fetch_url(url, params)

    bsc = bs(content)

    games = []

    base_url = bsc.baseimgurl.string
    for game in bsc.find_all('game'):
        try:
            date = game.releasedate.string
        except:
            date = 'N/A'
        try:
            overview = game.overview.string
        except:
            overview = 'N/A'
        try:
            cover_image = base_url + game.find('boxart', side="front").string
        except:
            cover_image = 'N/A'
        try:
            rating = game.esrb.string
        except:
            rating = 'N/A'
        d = {'game_id': game.id.string,
             'title': game.gametitle.string,
             'release_date': date,
             'platform': game.platform.string,
             'overview': overview,
             'rating': rating,
             'cover_image': cover_image,
             }
        games.append(d)

    # This could writes results into a file get_games_list_name_YYYYMMDD.txt
    # _write_results("get_games_list", content, name)

    # Currently returns results as a list of dictionaries for each game

    return games


def get_game_details_from_list(game_list):
    """With a list of games and their ids, return details of the game"""

    url = 'http://thegamesdb.net/api/GetGame.php'

    for game in game_list:
        content, encoding = _fetch_url(url, {'id': game['game_id']})
        bsc = bs(content)
        try:
            game['overview'] = bsc.find('overview').string
        except AttributeError:
            game['overview'] = ''
        print game

    return game_list


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
