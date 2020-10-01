import requests
r = requests.get(
    'http://api.dataatwork.org/v1/skills/4d70921065c00a293597936b693345aa/related_jobs',
)
print(r.text)