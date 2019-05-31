import requests
import datetime
from config import Config
from flask import abort
import re


def get_github_releases():
    releases_list = []
    for repo in Config.watch_github_releases:
        release = requests.get(url=f"https://api.github.com/repos/{repo}/releases/latest").json()

        if release.get('message', '') == 'Not Found':
            print(f"Warning: Could not find a release for {repo}...")
            continue

        if re.match("API rate limit exceeded", release.get('message', '')):
            print("FATAL: Github rate limit reached!")
            # TODO: Whats the correct code?
            abort(500)

        date = datetime.datetime.strptime(release['published_at'], "%Y-%m-%dT%H:%M:%S%z")
        release_age = (datetime.datetime.now(tz=datetime.timezone.utc) - date)
        print(f"The latest release of {repo} is {release['name']}")
        if release_age >= datetime.timedelta(days=7):
            print(f"    The release is {release_age.days} days old.")
            # continue

        releases_list.append({'name': release['name'], 'released': date, 'tag': release['tag_name'], 'repo': repo})
        sorted_releases = sorted(releases_list, key=lambda r: r['released'])
    return sorted_releases
