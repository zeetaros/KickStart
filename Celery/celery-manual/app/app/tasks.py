@shared_task
def fetch_hot_repos(since, per_page, page):
    payload = {
        'sort': 'stars', 'order': 'desc', 'q': 'created:>={date}'.format(date=since),
        'per_page': per_page, 'page': page,
        'access_token': settings.GITHUB_OAUTH}
    headers = {'Accept': 'application/vnd.github.v3+json'}
    connect_timeout, read_timeout = 5.0, 30.0
    r = requests.get(
        'https://api.github.com/search/repositories',
        params=payload,
        headers=headers,
        timeout=(connect_timeout, read_timeout))
    items = r.json()[u'items']
    return items